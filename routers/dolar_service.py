from fastapi import APIRouter
from starlette.responses import JSONResponse

from constants.constants import name_mapping
from data.cotizaciones import data

router = APIRouter(prefix="/dolar")


@router.get("/")
async def get_all():
    return data


@router.get("/{name}")
async def get_with_name(name: str):
    normalized_name = name.lower()
    if normalized_name in name_mapping:
        actual_name = name_mapping[normalized_name]
        response = {
            actual_name: data["cotizaciones"][actual_name],
            "actualizado": data["actualizado"],
        }
        return response

    else:
        return JSONResponse({"error": "Invalid name"}, status_code=404)
