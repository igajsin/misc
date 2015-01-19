#!/bin/bash

set -e

_env () (virsh net-list|grep admin|cut -d " " -f 2 | xargs echo -n)
_net () (xargs virsh net-info| grep Bridge|awk '{print $2}'|xargs ip a l|grep inet|awk '{print $2}')
_print() (sed s/\_admin/' '/)

_env |tee >(_net) | _print
