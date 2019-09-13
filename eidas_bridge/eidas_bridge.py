
# eidas_bridge.py
""" EIDAS BRIDGE """

from .utils.util import check_args
from .utils.crypto import PSS_PADDING
from .eidaslink import EIDASLink, EIDASProofException
from .eidas_service import EIDASService
from .verifiable_credential import VerifiableCredential
from .did_document import DIDDocument

class EIDASNotSupportedException(Exception):
    """
    Error raised when is called a library function than will not be supported 
    at this development Phase.
    """

class EIDASDIDMismatchException(Exception):
    """
    Error raised when the Issuer's DID differs from the DID_Document's DID subject.
    """

def eidas_link_did(did, certificate, proof, padding = PSS_PADDING) -> str:
    """ 
    Link the Issuer DID with eIDAS certificate

    Receives a DID, an eIDAS certificate, its proof of possession, and 
    optionally the padding of the signature proof (accepts PKCS#1 and PSS)

    Returns the JSON that needs to be stored on the Agent public Storage
    (i.e: an Identity Hub)
    """
    
    return EIDASLink(did, certificate, proof, padding).to_json()

def eidas_load_qec(did, qec, password=None):
    """
    Imports an eIDAS Qualified Electronic Certificate (QEC) with its correspondent 
    private key to be used in further digital signature operations.

    QEC currently supported format is only Secp256k1.
    """

def eidas_get_service_endpoint(did, service_endpoint) -> str:
    """ 
    Contructs the JSON structure that needs to be added to the Issuer's 
    DID Document Service Endpoint Section. 

    Receives a did and a service endpoint where it is stored the issuer's 
    eIDAS and DID linking information.

    Returns the correspondent JSON to be added to the Service Endpoint 
    Section of the Issuer's DID Document.
    """

    return EIDASService(did, service_endpoint).to_json()

def eidas_get_pubkey(did) -> str:
    """
    From a given DID, returns the correspondent public key.

    Cryptographic keys currently supported format are only Secp256k1.
    """

    return ""

def eidas_sign_credential(credential) -> str:
    """ 
    Adds a digital signature to the given credential, generated with an eIDAS private key.

    Returns the correspondent Verifiable Credential.

    Cryptographic keys currently supported format are only Secp256k1.
    """

    return ""

def eidas_verify_credential(credential, json_did_document) -> str:
    """
    Verifies that the credential issuer had a valid eIDAS certificate at the moment of issuing the passed credential. Throws EIDASProofException on signarure not valid.

    The current implementation does NOT support for DID resolution.

    The algorithm executes the following procedure:

    1. Get DID from the credential and from did_document and check they are the same
    2. Get EidasService service endpoint from did_document to be able to access the Issuer's Identity Hub
    3. Retrieve QEC from the Issuer's Identity Hub, check the certificate validity and extract its public key
    4. Verify credential signature with the extracted eIDAS public key
    5. Return VALID or throw EIDASProofException on signature not valid
    """

    # Constructs a Verifiable Credential object and gets the issuer's did
    verifiable_credential = VerifiableCredential(credential)
    did_from_cred = verifiable_credential.get_issuer_did()

    # Constructs a DID Document object ang gets the did subject
    did_document = DIDDocument(json_did_document)
    did_from_doc = did_document.get_did()

    if not did_from_cred == did_from_doc:
        raise EIDASDIDMismatchException("Issuer's DID differs from the DID_Document's DID subject")
    
    # Creates an EIDAS Service Endpoint to retrieve the EIDAS Link DID Structure 
    eidas_service = did_document.get_eidas_service_endpoint()
    # checks the signature in the EIDAS Link constructor
    # Throws EIDASProofException on signarure not valid
    EIDASLink.from_json(eidas_service.get_eidas_link_did())

    return "VALID"