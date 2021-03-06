# -*- coding: utf-8 -*-
import os

TF_FOLDER = "build/terraform"
TFVARS_JSON_NAME = "terraform.tfvars.json"
IMAGE_FOLDER = "/tmp/images"
STORAGE_PATH = "/var/lib/libvirt/openshift-images"
SSH_KEY = "ssh_key/key.pub"
NODES_REGISTERED_TIMEOUT = 600
CLUSTER_INSTALLATION_TIMEOUT = 60 * 30  # 30 minutes
START_CLUSTER_INSTALLATION_TIMEOUT = 360
TF_TEMPLATE = "terraform_files"
NUMBER_OF_MASTERS = 3
TEST_INFRA = "test-infra"
CLUSTER = CLUSTER_PREFIX = "%s-cluster" % TEST_INFRA
TEST_NETWORK = "test-infra-net-"
TEST_SECONDARY_NETWORK = "test-infra-secondary-network-"
DEFAULT_CLUSTER_KUBECONFIG_PATH = "build/kubeconfig"
WAIT_FOR_BM_API = 900
NAMESPACE_POOL_SIZE = 15


class NodeRoles:
    WORKER = "worker"
    MASTER = "master"


class NodesStatus:
    INSUFFICIENT = "insufficient"
    KNOWN = "known"
    INSTALLING = "installing"
    INSTALLING_IN_PROGRESS = "installing-in-progress"
    INSTALLED = "installed"
    ERROR = "error"
    PENDING_FOR_INPUT = "pending-for-input"


class ClusterStatus:
    INSTALLED = "installed"
    READY = "ready"
    INSTALLING = "installing"
