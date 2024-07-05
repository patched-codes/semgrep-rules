# License: MIT (c) GitLab Inc.
# source: https://github.com/PyCQA/bandit/blob/main/examples/logging_config_insecure_listen.py (incl modifications)

import logging
from logging import config as aliased_cfg

# ruleid: python_log_rule-logging-config-insecure-listen
logging.config.listen(9999) # FAIL
# ruleid: python_log_rule-logging-config-insecure-listen
aliased_cfg.listen(8888) # FAIL
