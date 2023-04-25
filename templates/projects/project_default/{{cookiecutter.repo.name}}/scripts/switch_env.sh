#!/bin/sh

ENV_NAME={{cookiecutter.interpreter.conda.env.name}}
VENV_PATH={{cookiecutter.interpreter.venv.dev}}


usage() { 
  echo "Usage for $(basename $0):"
  echo "$(basename $0) -h  enables help usage menu"
  echo "$(basename $0) should be run via sourcing it as below:"
  # e.g., source the script
  echo ". $(basename $0)"
}

while getopts ":hp:" opt; do
    case ${opt} in
      h)
        usage
        exit 0
        ;;
      p)
        profile=${OPTARG}
        echo "Set Profile for SSH: ${profile}"
        ;;
      \?)
        echo "Unknown Command Option: -$OPTARG, See Usage..." 1>&2
        usage
        exit 1
        ;;
      :)
        echo "Option -$OPTARG requires an argument." 1>&2
        usage
        exit 1
        ;;
    esac 
done
shift $((OPTIND -1))



source $(conda info --base)/etc/profile.d/conda.sh && conda activate ${ENV_NAME}
source ${VENV_PATH}/bin/activate 
