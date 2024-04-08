import os

import hydra
from dotenv import load_dotenv
from omegaconf import DictConfig

from evaluations.evaluation import Evaluation


load_dotenv(".env.email")
PROJECT_ROOT = os.getenv("EVALUATION_SYSTEM_ROOT")
if not PROJECT_ROOT:
    raise RuntimeError("Run ../set_proj_root.sh to set env var EVALUATION_SYSTEM_ROOT")


def config_is_valid(conf: DictConfig):
    """Checks if the config schema is valid

    Args:
        config (dict): the hydra (yaml) config.
    """
    return True


@hydra.main(
    version_base=None,
    config_path=f"{PROJECT_ROOT}/artsentry_ai_evaluation_system/configs",
    config_name="evaluation_run",
)
def main(cfg: DictConfig):
    if not config_is_valid(cfg):
        raise RuntimeError("The cfg supplied is not valid.")

    evaluation = Evaluation(cfg)
    evaluation.run()


if __name__ == "__main__":
    main()
