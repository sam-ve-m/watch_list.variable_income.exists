from unittest.mock import patch, AsyncMock

import pytest
from etria_logger import Gladsheim
from nidavellir import Sindri
from pytest import mark

from src.domain.request.model import WatchListSymbol
from src.domain.watch_list.model import WatchListSymbolModel
from src.repositories.watch_list.repository import WatchListRepository

dummy_symbol_to_insert = {"symbol": "PETR4", "region": "BR"}

dummy_watch_list_symbol_model = WatchListSymbolModel(
    WatchListSymbol(**dummy_symbol_to_insert), "test_id"
)
dummy_insert = str(
    Sindri.dict_to_primitive_types(dummy_watch_list_symbol_model.to_dict())
)


@mark.asyncio
@patch.object(WatchListRepository, "_WatchListRepository__get_collection")
async def test_exists(get_collection_mock):
    collection_mock = AsyncMock()
    collection_mock.find_one.return_value = True
    get_collection_mock.return_value = collection_mock
    result = await WatchListRepository.exists(dummy_watch_list_symbol_model)
    collection_mock.find_one.assert_called_with(
        {"_id": dummy_watch_list_symbol_model.get_id()}
    )
    assert result


@mark.asyncio
@patch.object(Gladsheim, "error")
@patch.object(WatchListRepository, "_WatchListRepository__get_collection")
async def test_exists_exception(get_collection_mock, etria_mock):
    collection_mock = AsyncMock()
    collection_mock.find_one.side_effect = Exception("erro")
    get_collection_mock.return_value = collection_mock
    with pytest.raises(Exception):
        result = await WatchListRepository.exists(dummy_watch_list_symbol_model)
        assert etria_mock.called
