import pytest
from src.main.schema import PageResponse


def test_page_response_eq_not_same_type():
    page_1 = PageResponse(
        page_number=1, page_size=1, total_pages=1, total_record=0, content={}
    )
    with pytest.raises(TypeError):
        page_1 == list()


def test_page_response_eq_true():
    page_1 = PageResponse(
        page_number=1, page_size=1, total_pages=1, total_record=0, content={}
    )
    page_2 = PageResponse(
        page_number=1, page_size=1, total_pages=1, total_record=0, content={}
    )
    assert page_1 == page_2


def test_page_response_eq_false():
    page_1 = PageResponse(
        page_number=1, page_size=1, total_pages=1, total_record=0, content={}
    )
    page_2 = PageResponse(
        page_number=2, page_size=1, total_pages=1, total_record=0, content={}
    )
    assert page_1 != page_2
