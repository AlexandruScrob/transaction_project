from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.settings import get_settings
from crud.engine import init_db
from orders.views import router as orders_router
from transactions.views import router as transactions_router


settings = get_settings()


app = FastAPI(
    title="Aplicatie Tranzactii",
    description="Examplu de aplicatie cu tranzactii.",
    version="0.0.1",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


###
# Register startup events
###
@app.on_event("startup")
def startup_event():
    init_db(settings.db_path)


###
# Register routers
###
app.include_router(orders_router, tags=["Order"])
app.include_router(transactions_router, tags=["Transaction"])
