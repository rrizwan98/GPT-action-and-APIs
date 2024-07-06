from db import get_all_products, get_product_by_name_or_id, add_product, update_product, delete_product
from fastapi import FastAPI, HTTPException, APIRouter
from models import ProductUpdate, Product
from fastapi import HTTPException, Request
from pydantic import BaseModel
from typing import Union

router = APIRouter()

@router.get("/products")
def read_products():
    """ Endpoint to fetch all products """
    try:
        return get_all_products().to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/product")
def read_product(name: Union[str, None] = None, product_id: Union[int, None] = None):
    """ Endpoint to fetch a product by name or ID """
    if not name and not product_id:
        raise HTTPException(status_code=400, detail="Please provide a product name or ID.")
    try:
        result = get_product_by_name_or_id(name, product_id)
        if result.empty:
            raise HTTPException(status_code=404, detail="Product not found.")
        return result.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/add_product")
def create_product(product_details: Product):
    """ Endpoint to add a new product """
    try:
        response = add_product(product_details.dict())
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/update_product/{product_name}")
def update_product_details(product_name: str, product_update: ProductUpdate):
    """ Endpoint to update a product by name """
    try:
        response = update_product(product_name, product_update.dict(exclude_none=True))
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/delete_product/{product_name}")
def delete_product_endpoint(product_name: str):
    """ Endpoint to delete a product by name """
    try:
        response = delete_product(product_name)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))