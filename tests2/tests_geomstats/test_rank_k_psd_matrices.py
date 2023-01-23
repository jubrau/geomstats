import random

import pytest

from geomstats.geometry.rank_k_psd_matrices import (
    BuresWassersteinBundle,
    RankKPSDMatrices,
)
from geomstats.test.geometry.rank_k_psd_matrices import (
    BuresWassersteinBundleTestCase,
    RankKPSDMatricesTestCase,
)
from geomstats.test.parametrizers import DataBasedParametrizer
from tests2.data.rank_k_psd_matrices_data import (
    BuresWassersteinBundleTestData,
    RankKPSDMatricesTestData,
)


def _get_random_params():
    while True:
        a = random.randint(2, 6)
        b = random.randint(2, 6)

        if a != b:
            break

    if a > b:
        n, k = a, b
    else:
        n, k = b, a

    return n, k


@pytest.fixture(
    scope="class",
    params=[
        (3, 2),
        _get_random_params(),
    ],
)
def spaces(request):
    n, k = request.param
    request.cls.space = RankKPSDMatrices(n=n, k=k)


@pytest.mark.usefixtures("spaces")
class TestRankKPSDMatrices(RankKPSDMatricesTestCase, metaclass=DataBasedParametrizer):
    testing_data = RankKPSDMatricesTestData()


@pytest.fixture(
    scope="class",
    params=[
        (3, 2),
        _get_random_params(),
    ],
)
def bundle_spaces(request):
    n, k = request.param
    request.cls.base = RankKPSDMatrices(n=n, k=k)
    request.cls.space = BuresWassersteinBundle(n, k)


@pytest.mark.usefixtures("bundle_spaces")
class TestBuresWassersteinBundle(
    BuresWassersteinBundleTestCase, metaclass=DataBasedParametrizer
):
    testing_data = BuresWassersteinBundleTestData()
