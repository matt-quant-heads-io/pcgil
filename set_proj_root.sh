# Sets the env var EVALUATION_SYSTEM_ROOT to the directory of this file.
# This will integrate artsentry_ai_evaluation_system into a common namespace.
export PCGIL_SYSTEM_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
if [[ $0 == $BASH_SOURCE ]]; then 
        echo "source this script to set the PCGIL_SYSTEM_ROOT env var."     
else
        echo "EVALUATION_SYSTEM_ROOT is now $PCGIL_SYSTEM_ROOT"
fi
