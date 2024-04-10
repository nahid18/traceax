#  Copyright (c) 2024 MancusoLab.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from importlib.metadata import PackageNotFoundError, version  # pragma: no cover

from ._estimators import (
    AbstractTraceEstimator as AbstractTraceEstimator,
    HutchinsonEstimator as HutchinsonEstimator,
    HutchPlusPlusEstimator as HutchPlusPlusEstimator,
    XNysTraceEstimator as XNysTraceEstimator,
    XTraceEstimator as XTraceEstimator,
)
from ._samplers import (
    AbstractSampler as AbstractSampler,
    NormalSampler as NormalSampler,
    RademacherSampler as RademacherSampler,
    SphereSampler as SphereSampler,
)


try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
