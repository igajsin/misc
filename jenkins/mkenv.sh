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

function run_test () { # iso_path env_name workspace_path python_venv job_name
    echo running the test
    iso_path=$1
    env_name=$2
    workspace_path=$3
    python_venv=$4
    job_name=$5
    test_group=$6
    $fuel_qa/utils/jenkins/system_tests.sh -t test -w $workspace_path -e $env_name -o --group=$test_group -i $iso_path -V $python_venv -j $job_name -K

}

iso=$1
test_group=${2:-ha_neutron_mysql_termination}
workspace_path=${3:-~/fuel-qa}
env_name=${4:-fuel_system_test}
python_venv=${5:-~/fuel10}
job_name=${6:-verify-fuel-ui-on-fuel-web}


activate_venv $python_venv

create_env $iso $env_name

run_test $iso $env_name $workspace_path $python_venv $job_name $test_group
