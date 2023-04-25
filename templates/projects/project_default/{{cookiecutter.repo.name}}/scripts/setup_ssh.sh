#!/bin/sh

usage() { 
  echo "Usage for $(basename $0):"
  echo "$(basename $0) -h           enables help usage menu"
  # e.g., use aws for paraphrase 
  echo "$(basename $0) -p <profile> configures profile name argument for key generation; e.g. remote_cluster"
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


if [ -z "$profile" ]; then
    echo "ERROR: PROFILE is required."
    usage
    exit 1
fi


ssh_dir=$HOME/.ssh
mkdir -p ${ssh_dir}
key_file=$ssh_dir/${profile}_id_rsa

# Check if SSH key for profile already exists
if [[ -f ~/.ssh/${profile}_id_rsa ]]; then
  echo "SSH key for profile ${profile} already exists."
  echo "Skipping key generation and adding existing key to SSH."
else
  # Generate new SSH key
  echo "Generating new SSH key for profile ${profile}..."
  ssh-keygen -t rsa -b 4096 -C ${profile} -f ${key_file} -N ""
  cat ${key_file}.pub
fi

# kick off agent to add the key
eval "$(ssh-agent -s)"
# Add SSH key to SSH
echo "Adding SSH key for profile ${profile} to SSH..."
ssh-add ~/.ssh/${profile}_id_rsa
echo "SSH key for profile ${profile} has been added to SSH."
# copy public key to clipboard
pbcopy < ${key_file}.pub









