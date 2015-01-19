#!/bin/bash

set -e

_env () (virsh net-list|grep admin|cut -d " " -f 2)

_ip () (virsh net-info $1| grep Bridge|awk '{print $2}'|xargs ip a l|grep inet|awk '{print $2}')

for s in $(_env); do
    echo ${s%_admin}  $(_ip $s)
done
