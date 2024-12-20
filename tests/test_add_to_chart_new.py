import pytest
from Infrastructure.objects.objects_api.product_page_api import ProductPageApi
from Infrastructure.Infra.dal.api_access.api_accsess import ApiAccess


class TestSecondNew:
    url = "https://api.demoblaze.com/addtocart"

    @pytest.mark.regression
    def test_add_to_chart_new(self):
        # Step 1: Initialize ApiAccess
        api_access = ApiAccess()

        # Step 2: Initialize ProductPageApi with the ApiAccess instance
        product_page_api = ProductPageApi(api_access=api_access)

        # Step 3: Call the add_item_to_chart method
        product_page_api.add_item_to_chart(TestSecondNew.url)
