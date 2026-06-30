"""
    Phần 1: Báo cáo phân tích
    1. Input của bài toán

    Input là các Query Parameter người dùng gửi lên API:

    Input : keyword   | kiểu: string  | ý nghĩa: từ khóa tìm kiếm tên sản phẩm
            max_price | kiểu: float | ý nghĩa: giá tối đa để lọc sản phẩm

    Ví dụ:

    GET /products?keyword=mouse

    Input:

    keyword = "mouse"
    GET /products?max_price=1000000

    Input:

    max_price = 1000000
    2. Output mong muốn

    API trả về danh sách sản phẩm phù hợp điều kiện.

    Ví dụ:

    Request:

    GET /products?keyword=mouse

    Response:

    [
        {
            "id": 2,
            "name": "Mouse",
            "price": 200000
        }
    ]

    Nếu không có điều kiện:

    GET /products

    Trả về toàn bộ:

    [
        {
            "id":1,
            "name":"Laptop",
            "price":15000000
        }
    ]
    3. Giải pháp xử lý

    Các bước:

    Nhận keyword và max_price từ URL.
    Kiểm tra max_price:
    Nếu nhỏ hơn 0 → báo lỗi.
    Duyệt danh sách sản phẩm.
    Kiểm tra điều kiện:
    Nếu có keyword:
    kiểm tra tên sản phẩm có chứa keyword.
    Nếu có max_price:
    kiểm tra giá sản phẩm <= max_price.
    Trả về danh sách kết quả.
"""

from fastapi import FastAPI, Query, HTTPException

app = FastAPI()


products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 200000},
    {"id": 3, "name": "Keyboard", "price": 500000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]


@app.get("/products")
def get_products(
    keyword: str = Query(None),
    max_price: float = Query(None)
):

    # kiểm tra giá âm
    if max_price is not None and max_price < 0:
        raise HTTPException(
            status_code=400,
            detail="max_price không được âm"
        )


    result = products


    # lọc theo keyword
    if keyword:
        result = [
            product for product in result
            if keyword.lower() in product["name"].lower()
        ]


    # lọc theo giá
    if max_price is not None:
        result = [
            product for product in result
            if product["price"] <= max_price
        ]


    return result