from dataclasses import dataclass
from typing import List
from enum import Enum


class DeviceFamilyEnum(Enum):
    ProductFamily_UNKNOWN = 'ProductFamily_UNKNOWN'


class DeviceVariantEnum(Enum):
    ProductVariant_TUV = 'ProductVariant_TUV'
    ProductVariant_PDA = 'ProductVariant_PDA'


class DeviceModelEnum(Enum):
    ProductModel_ALLIANCEIS = 'ProductModel_ALLIANCEIS'


class ProductDetails:
    # The product model
    productModel: DeviceModelEnum
    # The product variant
    productVariant: DeviceVariantEnum
    # The product family
    productFamily: DeviceFamilyEnum
    # The product version
    productVersion: str
    # The system's serial number
    serial: str


class SoftwareDetails:
    # The software version
    version: str
    # The software build date
    buildDate: str


class SupportDetails:
    # The company name
    companyName: str
    # The street address
    companyAddress1: str
    # The city, state and zipcode
    companyAddress2: str
    # The country
    companyAddress3: str
    # The support website
    supportUrl: str


class LanguageDetails:
    # The language code
    language: str
    # The localized content
    content: str


class TermsDetails:
    # The language code
    language: str
    # The localized content
    content: str


@dataclass
class AboutResponse:
    # The hardware information
    hardware: ProductDetails
    # Software information
    software: SoftwareDetails
    # Support information, including company name, address and url
    support: SupportDetails
    # Localized text content used to return the EULA and Terms that are stored on the isym
    eula: List[LanguageDetails]
    # Localized text content used to return the EULA and Terms that are stored on the isym
    terms: List[TermsDetails]

    dataModelType: str
    dataModelVersion: int
