#!/bin/bash

set -ex

function activate_venv() { # venv path
    . $1/bin/activate
}


function create_env () { # iso_name env_name
    dos.py list|grep fuel_system_test || dos.py create-env default.yaml
}

function run_test () { # iso_path env_name workspace_path python_venv job_name
    iso_path=$1
    env_name=$2
    workspace_path=$3
    python_venv=$4
    job_name=$5
    test_group=$6
    $workspace_path/utils/jenkins/system_tests.sh -t test -w $workspace_path -e $env_name -o --group=$test_group -i $iso_path -V $python_venv -j $job_name
}

export ISO_PATH=$1
export test_group=${2:-ha_neutron_mysql_termination}
export workspace_path=${3:-~/fuel-qa}
export ENV_NAME=${4:-fuel_system_test}
export python_venv=${5:-~/fuel10}
export job_name=${6:-verify-fuel-ui-on-fuel-web}

export ADMIN_NODE_MEMORY=8192
export SLAVE_NODE_MEMORY=$ADMIN_NODE_MEMORY


activate_venv $python_venv

create_env $ISO_PATH $ENV_NAME

run_test $ISO_PATH  $ENV_NAME $workspace_path $python_venv $job_name $test_group
