# pylint: disable=line-too-long,missing-module-docstring
from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse, Response

from crud import transactions
from crud.interface import DBInterface
from crud.models import DBTransaction
from core.settings import get_settings

from transactions.helpers import check_headers
from transactions.serializers import TransactionModel
from transactions.responses import TransactionResponse, TransactionNotFound

router = APIRouter()
settings = get_settings()


@router.get(
    "/transaction/{transaction_id}",
    name="Get Transaction",
    dependencies=[Depends(check_headers)],
    responses={
        status.HTTP_200_OK: {"model": TransactionResponse},
        status.HTTP_404_NOT_FOUND: {"model": TransactionNotFound},
    },
)
def view_get_transaction(transaction_id: str) -> JSONResponse:
    """Retrieve transaction by a transaction ID or return a 404 not found

    Args:
        transaction_id (str): transaction ID

    Returns:
        Transaction details
    """
    transaction_interface = DBInterface(DBTransaction)
    transaction_response = transactions.get_transaction(transaction_id, transaction_interface)

    if transaction_response is None:
        return _handle_transaction_not_found(transaction_id)

    response_model = TransactionResponse(**transaction_response).dict(by_alias=True)
    return JSONResponse(status_code=status.HTTP_200_OK, content=response_model)


@router.get(
    "/transactions",
    name="Get all Transactions",
    dependencies=[Depends(check_headers)],
    responses={
        status.HTTP_200_OK: {"model": list[TransactionResponse]},
    },
)
def view_get_all_transactions() -> JSONResponse:
    """Retrieve all transactions present in the Table

    Returns:
        List of transactions and their details
    """
    transaction_interface = DBInterface(DBTransaction)
    transaction_response = transactions.get_all_transactions(transaction_interface)

    response_model = [TransactionResponse(**transaction).dict(by_alias=True) for transaction in transaction_response]
    return JSONResponse(status_code=status.HTTP_200_OK, content=response_model)


@router.post(
    "/transaction",
    name="Create Transaction",
    dependencies=[Depends(check_headers)],
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": TransactionResponse},
    },
)
def view_create_transaction(transaction_data: TransactionModel) -> JSONResponse:
    """Create a new transaction based on the request body

    Args:
        transaction_data (TransactionModel): transaction data

    Returns:
        New transaction details
    """
    transaction_interface = DBInterface(DBTransaction)
    transaction_response = transactions.create_transaction(transaction_data, transaction_interface)

    response_model = TransactionResponse(**transaction_response).dict(by_alias=True)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=response_model)


@router.patch(
    "/transaction/{transaction_id}",
    name="Update Transaction",
    dependencies=[Depends(check_headers)],
    responses={
        status.HTTP_200_OK: {"model": TransactionResponse},
        status.HTTP_404_NOT_FOUND: {"model": TransactionNotFound},
    },
)
def view_update_transaction(transaction_id: str, transaction_data: TransactionModel) -> JSONResponse:
    """Update an existing transaction with new details from the request body

    Args:
        transaction_id (str): transaction ID
        transaction_data (TransactionModel): transaction data

    Returns:
        Updated transaction details
    """
    transaction_interface = DBInterface(DBTransaction)
    transaction_response = transactions.update_transaction(transaction_id, transaction_data, transaction_interface)

    if transaction_response is None:
        return _handle_transaction_not_found(transaction_id)

    return JSONResponse(status_code=status.HTTP_200_OK, content=transaction_response)


@router.delete(
    "/transaction/{transaction_id}",
    name="Delete Transaction",
    dependencies=[Depends(check_headers)],
    responses={
        status.HTTP_200_OK: {"model": None},
        status.HTTP_404_NOT_FOUND: {"model": TransactionNotFound},
    },
)
def view_delete_transaction(transaction_id: str) -> Response:
    """Delete a transaction based on the transaction ID or return a 404 not found

    Args:
        transaction_id (str): transaction ID

    Returns:
        None
    """
    transaction_interface = DBInterface(DBTransaction)
    transaction_response = transactions.delete_transaction(transaction_id, transaction_interface)

    if transaction_response is None:
        return _handle_transaction_not_found(transaction_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


def _handle_transaction_not_found(transaction_id: str) -> JSONResponse:
    """Create a JSON response for the case we don't find a certain transaction based on their ID

    Args:
        transaction_id (str): transaction ID

    Returns:
        JSON response with custom not found message
    """
    response_model = TransactionNotFound(
        response_message=f"Transaction not found for transactionId: {transaction_id}"
    ).dict(by_alias=True)
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=response_model)
