#!/bin/bash

set -e
set -x

function activate_venv() { # venv path
    echo activating the venv
    . $1/bin/activate
}


function create_env () { # iso_name env_name
    echo creating the env $2
    iso=$1
    env_name=$2
    dos.py create -C 7 --ram 8192 --admin-disk-size 60 --second-disk-size 60  --third-disk-size 60 -I $iso $env_name
}

function run_test () { # iso_path env_name workspace_path fuel-qa_path python_venv job_name
    echo running the test
#    echo pyton path is $PYTHONPATH
    iso_path=$1
    env_name=$2
    workspace_path=$3
    fuel_qa=$4
    python_venv=$5
    job_name=$6
    $fuel_qa/utils/jenkins/system_tests.sh -t test -w $workspace_path -e $env_name -o --group=bvt_2 -i $iso_path -V $python_venv -j $job_name -K

}

iso=$1
env_name=${2:-fuel_system_test}
fuel_qa=${4:-~/fuel-qa}
workspace_path=${3:-~/fuel-qa}
python_venv=${5:-~/fuel10}
#job_name=${6:-verify-fuel-ui-on-fuel-web}
job_name=${6:-10.0.system_test.ubuntu.ha_neutron_destructive}

#export PATH=$fuel_qa:$PATH
#export PYTHONPATH=$fuel_qa:$PYTHONPATH

activate_venv $python_venv

create_env $iso $env_name

run_test $iso $env_name $workspace_path $fuel_qa $python_venv $job_name
