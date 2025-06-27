from dataclasses import dataclass

from isym_test_api.rest_api.api.behavior.system_meta_method_request import SystemMetaMethodRequest, generate_default_system_meta_method_request


@dataclass
class SystemNonInjectRuntimeMetadata:
    runTimeMin: float


@dataclass
class SystemMetaWetPrimeMetadataRequest:
    systemMethod: SystemMetaMethodRequest
    runTime: SystemNonInjectRuntimeMetadata


def generate_default_system_wet_prime_request():
    method_request = generate_default_system_meta_method_request()
    payload = SystemMetaWetPrimeMetadataRequest(systemMethod=method_request, runTime=SystemNonInjectRuntimeMetadata(runTimeMin=5.0))
    return payload
