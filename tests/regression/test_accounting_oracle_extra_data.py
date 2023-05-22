import pytest
from utils.test.extra_data import ExtraDataService
from utils.test.oracle_report_helpers import oracle_report

from utils.config import MAX_ACCOUNTING_EXTRA_DATA_LIST_ITEMS_COUNT, MAX_NODE_OPERATORS_PER_EXTRA_DATA_ITEM_COUNT


@pytest.fixture()
def extra_data_service():
    return ExtraDataService()


def test_accounting_oracle_too_node_ops_per_extra_data_item(extra_data_service):
    nos_per_item_count = 30
    item_count = MAX_ACCOUNTING_EXTRA_DATA_LIST_ITEMS_COUNT
    extra_data = extra_data_service.collect(
        {(1, i): i for i in range(nos_per_item_count)},
        {(1, i): i for i in range(nos_per_item_count)},
        item_count,
        nos_per_item_count,
    )

    oracle_report(
        extraDataFormat=1,
        extraDataHash=extra_data.data_hash,
        extraDataItemsCount=item_count,
        extraDataList=extra_data.extra_data,
    )