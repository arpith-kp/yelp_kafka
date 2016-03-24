import mock
import pytest

from yelp_kafka.config import ClusterConfig
from yelp_kafka.config import KafkaConsumerConfig


@pytest.fixture
def cluster():
    return ClusterConfig(
        'cluster_type', 'mycluster', ['test_broker:9292'], 'test_cluster'
    )


@pytest.fixture
def mock_pre_rebalance_cb():
    return mock.Mock()


@pytest.fixture
def mock_post_rebalance_cb():
    return mock.Mock()


@pytest.fixture
def config(
    cluster,
    mock_pre_rebalance_cb,
    mock_post_rebalance_cb
):
    return KafkaConsumerConfig(
        cluster=cluster,
        group_id='test_group',
        client_id='test_client_id',
        partitioner_cooldown=0.5,
        pre_rebalance_callback=mock_pre_rebalance_cb,
        post_rebalance_callback=mock_post_rebalance_cb
    )
