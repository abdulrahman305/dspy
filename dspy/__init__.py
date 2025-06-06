import dspy.retrievers
from dspy.clients import DSPY_CACHE
from dspy.dsp.colbertv2 import ColBERTv2
from dspy.dsp.utils.settings import settings
from dspy.predict import *
from dspy.primitives import *
from dspy.retrieve import *
from dspy.signatures import *
from dspy.streaming.streamify import streamify
from dspy.teleprompt import *
from dspy.utils.asyncify import asyncify
from dspy.utils.logging_utils import (
    configure_dspy_loggers,
    disable_logging,
    enable_logging,
)
from dspy.utils.saving import load
from dspy.utils.usage_tracker import track_usage

from .__metadata__ import (
    __author__,
    __author_email__,
    __description__,
    __name__,
    __url__,
    __version__,
)

from dspy.adapters import (  # isort: skip
    Adapter,
    Audio,
    BaseType,
    ChatAdapter,
    History,
    Image,
    JSONAdapter,
    Tool,
    ToolCalls,
    TwoStepAdapter,
)

from dspy.evaluate import Evaluate  # isort: skip
from dspy.clients import *  # isort: skip

configure_dspy_loggers(__name__)

# from dspy.dsp.you import You

configure = settings.configure
context = settings.context

BootstrapRS = BootstrapFewShotWithRandomSearch

cache = DSPY_CACHE
