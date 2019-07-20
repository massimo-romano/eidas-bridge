# common_data.py
""" Data to used alongside the test suite """

from eidas_bridge.utils.crypto import PKCS1v15_PADDING, PSS_PADDING

dids = [
    "did:sov:55GkHamhTU1ZbTbV2ab9DE"
]

"""
eidas_link_inputs = [
    (
        b'-----BEGIN CERTIFICATE-----\n\
MIIDYDCCAkigAwIBAgIUK2iqE3mA/IKP0tw6vZpHu2BDgx0wDQYJKoZIhvcNAQEL\n\
BQAwXTELMAkGA1UEBhMCRVMxEzARBgNVBAgMClRFU1RfU1RBVEUxEjAQBgNVBAcM\n\
CVRFU1RfQ0lUWTEQMA4GA1UECgwHQ0FfQUNNRTETMBEGA1UEAwwKbXlzaXRlLmNv\n\
bTAeFw0xOTA3MDkxNDExMzFaFw0yMDA3MDgxNDExMzFaMF0xCzAJBgNVBAYTAkVT\n\
MRMwEQYDVQQIDApURVNUX1NUQVRFMRIwEAYDVQQHDAlURVNUX0NJVFkxEDAOBgNV\n\
BAoMB0NBX0FDTUUxEzARBgNVBAMMCm15c2l0ZS5jb20wggEiMA0GCSqGSIb3DQEB\n\
AQUAA4IBDwAwggEKAoIBAQCkBTDVrIS8z3xLUvPJgw6KfLQNcAnjUGKCm31D4ug6\n\
DP/+As6yXyv9ZvantidaqLbvom6RXcbD6b4lohyqr9MZCg7HcFmRiHbovcpPrt05\n\
PQ5QuFKeKWWEMUGMbXaBVCPb8Q2VbAnw1nzhRspcyDnUhY3HaeeroGpPBra/G+vi\n\
R5AeOH4WsjSIp7FGJXcd5P6Pizsg5SUyBVMXHeDyBkPp7OEUskyBN6jRnSaCpFZZ\n\
rKvHHntHIv2f5Q9esfma++bvEhqCGflgiWO+NtCqOs1ueJpPPSLiDQanx7SK5Gyu\n\
2N8/1mMZsvXR5Ae92eDicIHJdoUyEYmBWr8v1eJvDInfAgMBAAGjGDAWMBQGA1Ud\n\
EQQNMAuCCWxvY2FsaG9zdDANBgkqhkiG9w0BAQsFAAOCAQEAAnKpcJ64CiXGRw13\n\
sUnX9xHKSulyNt4BS5LYjoWC1tyQ9FH4kjD5WdFs9VOY89rOwGg1XlpjgJU5tM0i\n\
uv1J3SPM4ChR81XxxJaJ+ctz4CT2JO1YjLh2daONA9/pTGJgJBa476L9QhkrB1EX\n\
hRHPeFticEePQEp8lrkdTx4uCdF0FLnPSoh9HUQshDrzSTKW8kWwz7ghu5ZFafmD\n\
TdjhfyIB1Njvb76qlF1CsJHLD4OxVKXIlaoqOD9qQu42c0tNMfQZpsZI287BjpGm\n\
/0NrZQ46KDrlewPJdlVXXFEyKJyGnnaU8w8hOmLoNlkFgoCY0GOi6DUgeZ7HVWNf\n\
2/e1Dw==\n\
-----END CERTIFICATE-----\n',
    '6f95598f245e9fdc8b6e55c54c4b9a64f85e36147f67cb5cd1c6ee9b98fb3b97599eedc73b8097dad4d7b766d457c6138dc02dfddca59f1d08ccc4011625378970565bf7131928a1d36224a983156852d0218d3d21e20aadf79ff1ed1fbe880ac718d9550403dba119cdcc1a3a6a2fffc154cd03c305f2fab508037c93f1fee17bef98eab2a6bd9210cdd7e665dc9745c56de9a6204bd148577582ef3ec81858e3dc11c854d414dbbfb32846b95fa54573686ac334189f0beefba1012d2f77343b51855fe58725640bcc11532082e759c53848c395e6290ed0c1b7f062af9d0ab9dbd950dfc4a5594cee996c0ec3590d819f603ebb9586f0b54ac23c84967caf',
    PSS_PADDING,
    "did:sov:55GkHamhTU1ZbTbV2ab9DE"
    ),
    (
        b'-----BEGIN CERTIFICATE-----\n\
MIIDYDCCAkigAwIBAgIUK2iqE3mA/IKP0tw6vZpHu2BDgx0wDQYJKoZIhvcNAQEL\n\
BQAwXTELMAkGA1UEBhMCRVMxEzARBgNVBAgMClRFU1RfU1RBVEUxEjAQBgNVBAcM\n\
CVRFU1RfQ0lUWTEQMA4GA1UECgwHQ0FfQUNNRTETMBEGA1UEAwwKbXlzaXRlLmNv\n\
bTAeFw0xOTA3MDkxNDExMzFaFw0yMDA3MDgxNDExMzFaMF0xCzAJBgNVBAYTAkVT\n\
MRMwEQYDVQQIDApURVNUX1NUQVRFMRIwEAYDVQQHDAlURVNUX0NJVFkxEDAOBgNV\n\
BAoMB0NBX0FDTUUxEzARBgNVBAMMCm15c2l0ZS5jb20wggEiMA0GCSqGSIb3DQEB\n\
AQUAA4IBDwAwggEKAoIBAQCkBTDVrIS8z3xLUvPJgw6KfLQNcAnjUGKCm31D4ug6\n\
DP/+As6yXyv9ZvantidaqLbvom6RXcbD6b4lohyqr9MZCg7HcFmRiHbovcpPrt05\n\
PQ5QuFKeKWWEMUGMbXaBVCPb8Q2VbAnw1nzhRspcyDnUhY3HaeeroGpPBra/G+vi\n\
R5AeOH4WsjSIp7FGJXcd5P6Pizsg5SUyBVMXHeDyBkPp7OEUskyBN6jRnSaCpFZZ\n\
rKvHHntHIv2f5Q9esfma++bvEhqCGflgiWO+NtCqOs1ueJpPPSLiDQanx7SK5Gyu\n\
2N8/1mMZsvXR5Ae92eDicIHJdoUyEYmBWr8v1eJvDInfAgMBAAGjGDAWMBQGA1Ud\n\
EQQNMAuCCWxvY2FsaG9zdDANBgkqhkiG9w0BAQsFAAOCAQEAAnKpcJ64CiXGRw13\n\
sUnX9xHKSulyNt4BS5LYjoWC1tyQ9FH4kjD5WdFs9VOY89rOwGg1XlpjgJU5tM0i\n\
uv1J3SPM4ChR81XxxJaJ+ctz4CT2JO1YjLh2daONA9/pTGJgJBa476L9QhkrB1EX\n\
hRHPeFticEePQEp8lrkdTx4uCdF0FLnPSoh9HUQshDrzSTKW8kWwz7ghu5ZFafmD\n\
TdjhfyIB1Njvb76qlF1CsJHLD4OxVKXIlaoqOD9qQu42c0tNMfQZpsZI287BjpGm\n\
/0NrZQ46KDrlewPJdlVXXFEyKJyGnnaU8w8hOmLoNlkFgoCY0GOi6DUgeZ7HVWNf\n\
2/e1Dw==\n\
-----END CERTIFICATE-----\n',
    '828b50fe4b566442fab68a8f1f5dfd5d103878f6f1db22bd96aeb6d3d6e13b4505ab978eb0a9d2dbadfd81b37857c5097b4762d341857c11f70beb41efc70ba39daa5e560d7e411ff78723585f14b469c7c6df09a264ea303dd54b4eb491fdeba5398ac323ff637173cb1e6c12c4f18e5b026b71a2fab724780e912d07e217032273d58128e8a4d5fe9702a782e73f14debee7fa87e2abb08aadc152b3dc65a54c9e80a0a465252d207c38b5f56bcfb79bd2c02c08d9776871d61a697ff91691717c9392ada43996cdd7b258e21d49ae09627b19db2170727393eba37a5c83ca6e5ae95daad039b93cc775bca31e5764f6ead3961fbdfddc506d5e9f8f212405',
    PSS_PADDING,
    "did:sov:55GkHamhTU1ZbTbV2ab9DE"
    ),
    (
        b'-----BEGIN CERTIFICATE-----\n\
MIIDYDCCAkigAwIBAgIUK2iqE3mA/IKP0tw6vZpHu2BDgx0wDQYJKoZIhvcNAQEL\n\
BQAwXTELMAkGA1UEBhMCRVMxEzARBgNVBAgMClRFU1RfU1RBVEUxEjAQBgNVBAcM\n\
CVRFU1RfQ0lUWTEQMA4GA1UECgwHQ0FfQUNNRTETMBEGA1UEAwwKbXlzaXRlLmNv\n\
bTAeFw0xOTA3MDkxNDExMzFaFw0yMDA3MDgxNDExMzFaMF0xCzAJBgNVBAYTAkVT\n\
MRMwEQYDVQQIDApURVNUX1NUQVRFMRIwEAYDVQQHDAlURVNUX0NJVFkxEDAOBgNV\n\
BAoMB0NBX0FDTUUxEzARBgNVBAMMCm15c2l0ZS5jb20wggEiMA0GCSqGSIb3DQEB\n\
AQUAA4IBDwAwggEKAoIBAQCkBTDVrIS8z3xLUvPJgw6KfLQNcAnjUGKCm31D4ug6\n\
DP/+As6yXyv9ZvantidaqLbvom6RXcbD6b4lohyqr9MZCg7HcFmRiHbovcpPrt05\n\
PQ5QuFKeKWWEMUGMbXaBVCPb8Q2VbAnw1nzhRspcyDnUhY3HaeeroGpPBra/G+vi\n\
R5AeOH4WsjSIp7FGJXcd5P6Pizsg5SUyBVMXHeDyBkPp7OEUskyBN6jRnSaCpFZZ\n\
rKvHHntHIv2f5Q9esfma++bvEhqCGflgiWO+NtCqOs1ueJpPPSLiDQanx7SK5Gyu\n\
2N8/1mMZsvXR5Ae92eDicIHJdoUyEYmBWr8v1eJvDInfAgMBAAGjGDAWMBQGA1Ud\n\
EQQNMAuCCWxvY2FsaG9zdDANBgkqhkiG9w0BAQsFAAOCAQEAAnKpcJ64CiXGRw13\n\
sUnX9xHKSulyNt4BS5LYjoWC1tyQ9FH4kjD5WdFs9VOY89rOwGg1XlpjgJU5tM0i\n\
uv1J3SPM4ChR81XxxJaJ+ctz4CT2JO1YjLh2daONA9/pTGJgJBa476L9QhkrB1EX\n\
hRHPeFticEePQEp8lrkdTx4uCdF0FLnPSoh9HUQshDrzSTKW8kWwz7ghu5ZFafmD\n\
TdjhfyIB1Njvb76qlF1CsJHLD4OxVKXIlaoqOD9qQu42c0tNMfQZpsZI287BjpGm\n\
/0NrZQ46KDrlewPJdlVXXFEyKJyGnnaU8w8hOmLoNlkFgoCY0GOi6DUgeZ7HVWNf\n\
2/e1Dw==\n\
-----END CERTIFICATE-----\n',
    '72ef73a920c03361a408464ab566d8b429baee8517f5d293bec13fbcbe214921309ab54ccd4a9c7961b06c55dfb173686f4f50bc576f31f26b5c6048d4c13a60aa9bf7a3f7a007a76f31c5c867bcc23847576b482ec5dfeed0a3b04b976837d358245a2967b2560cb9431513bb57a13eff406654eeedf0746a7d8bcc4d55f4920b6dea014796da2d09a4867684a590d71435dcb22077954f229be647a20d044c1a4c964c8c67beb828449a6413187aa3f003bc5038b3d84a80b9ca64a618767155701b9b2429b01f53d0f0e1ef87a681092bc2d7edde41df31783abac39472cffac14c9e75aa70d2c4e55db28b9bff0caf00dabf3651ea23e6f26fe2b06be17e',
    PSS_PADDING,
    "did:sov:55GkHamhTU1ZbTbV2ab9DE"
    ),
"""
eidas_link_inputs = [
    (
        b'-----BEGIN CERTIFICATE-----\nMIIDYDCCAkigAwIBAgIUI63ffVceaNc1kN9O0q/4jSjbkU0wDQYJKoZIhvcNAQEL\nBQAwXTELMAkGA1UEBhMCRVMxEzARBgNVBAgMClRFU1RfU1RBVEUxEjAQBgNVBAcM\nCVRFU1RfQ0lUWTEQMA4GA1UECgwHQ0FfQUNNRTETMBEGA1UEAwwKbXlzaXRlLmNv\nbTAeFw0xOTA3MDkxNDA3MjBaFw0yMDA3MDgxNDA3MjBaMF0xCzAJBgNVBAYTAkVT\nMRMwEQYDVQQIDApURVNUX1NUQVRFMRIwEAYDVQQHDAlURVNUX0NJVFkxEDAOBgNV\nBAoMB0NBX0FDTUUxEzARBgNVBAMMCm15c2l0ZS5jb20wggEiMA0GCSqGSIb3DQEB\nAQUAA4IBDwAwggEKAoIBAQDm6RhyIeFZHn4bGQ/2UQ+aflczCo3Ej04LJXfiIU1Q\nt7xRq3e+uh7nTLffnS7fj/ZZBBREmR/D/SJBTlxv7WQEbscV/pf2LoZLjoC4M4ye\n43lUHRmWsm4J50tu9zcSheqXCRyAK/Ai6RUBy86NKXMFTUp/ONxS0BxJg8GU03Xd\nXGnYzdmZZXGDnublGYq03gD/cZYguS7/HS8v/MckdmjYPTy2syGL9unYkjWn7vig\niaDc2leAM4agKB6PODJSFla15HLoqskKX1SgtLJUHxu/FOo6hYdCt+GxpV1xhl/r\nEf3/SFeTZrJgL11m5ABDli2zAmCn4bjBNnNcXWy5QV0pAgMBAAGjGDAWMBQGA1Ud\nEQQNMAuCCWxvY2FsaG9zdDANBgkqhkiG9w0BAQsFAAOCAQEAYPUn0TzGyn438++1\nV2jMHC653C8tn3vVF5nTT7Td+ihc+KaaNDYsgyY2JpBIMRwlNgoNU0Da3P/9ZDn3\nlFJElUg8WpWPvpXtbS4udqn6UcfT9mFJtkzKg3CK5i50GRCabV9FPbY1bzYtUbY+\nEntXtI2h0dxcgzgOw6pkXFB3O7ZbbshpqWTlHtTtbxxrOFq0zcpyS92G+NTF6ASS\nhXcIf90du/mBWd2dinF/w2nkRAWfGBy8bGnUSJ93rPVwLjI0PDeHh7+PSQ+3X6mG\n5DI9EmzEC7esW6wJbhgiOYXLavAOmLfI0yq/z8SZMvFYwBE69VuGfPSj/u4nIhA5\nK0Qgnw==\n-----END CERTIFICATE-----\n',
        '4f1bb7069e1508901e83d9dd71043e35fbc8ecf3077625206dd00cf8f12365096cc1cf07822479e571689bc67c50a7d9ca66c43865e490044729af3356e853073073c11e9fa517f7b35748146c1c1101406f66866969ad5915054e3633ab3c247d6b09be909ece6d018ad309b1b34c45b223227d74928278640e0e6a62de0309309e609e8927eb7abd098dfb8a30e8c91fde3ea4fbe804b2967db2c994d303de1e6ac837cfd2a11414ace2bd75148e917b3505f17fabc4805484164a69fdc1d28122e977c1fa4f62b39a601915d8fe0b1bd6e2932db6c8ca3b2bca3ab04f3aebf83d081122d42248dc2a2f292f2c2bfc42244c3118109ab9f001a85cbdd52f71',
        PSS_PADDING,
        "did:sov:55GkHamhTU1ZbTbV2ab9DE"
    ),
    (
        b'-----BEGIN CERTIFICATE-----\nMIIDYDCCAkigAwIBAgIUI63ffVceaNc1kN9O0q/4jSjbkU0wDQYJKoZIhvcNAQEL\nBQAwXTELMAkGA1UEBhMCRVMxEzARBgNVBAgMClRFU1RfU1RBVEUxEjAQBgNVBAcM\nCVRFU1RfQ0lUWTEQMA4GA1UECgwHQ0FfQUNNRTETMBEGA1UEAwwKbXlzaXRlLmNv\nbTAeFw0xOTA3MDkxNDA3MjBaFw0yMDA3MDgxNDA3MjBaMF0xCzAJBgNVBAYTAkVT\nMRMwEQYDVQQIDApURVNUX1NUQVRFMRIwEAYDVQQHDAlURVNUX0NJVFkxEDAOBgNV\nBAoMB0NBX0FDTUUxEzARBgNVBAMMCm15c2l0ZS5jb20wggEiMA0GCSqGSIb3DQEB\nAQUAA4IBDwAwggEKAoIBAQDm6RhyIeFZHn4bGQ/2UQ+aflczCo3Ej04LJXfiIU1Q\nt7xRq3e+uh7nTLffnS7fj/ZZBBREmR/D/SJBTlxv7WQEbscV/pf2LoZLjoC4M4ye\n43lUHRmWsm4J50tu9zcSheqXCRyAK/Ai6RUBy86NKXMFTUp/ONxS0BxJg8GU03Xd\nXGnYzdmZZXGDnublGYq03gD/cZYguS7/HS8v/MckdmjYPTy2syGL9unYkjWn7vig\niaDc2leAM4agKB6PODJSFla15HLoqskKX1SgtLJUHxu/FOo6hYdCt+GxpV1xhl/r\nEf3/SFeTZrJgL11m5ABDli2zAmCn4bjBNnNcXWy5QV0pAgMBAAGjGDAWMBQGA1Ud\nEQQNMAuCCWxvY2FsaG9zdDANBgkqhkiG9w0BAQsFAAOCAQEAYPUn0TzGyn438++1\nV2jMHC653C8tn3vVF5nTT7Td+ihc+KaaNDYsgyY2JpBIMRwlNgoNU0Da3P/9ZDn3\nlFJElUg8WpWPvpXtbS4udqn6UcfT9mFJtkzKg3CK5i50GRCabV9FPbY1bzYtUbY+\nEntXtI2h0dxcgzgOw6pkXFB3O7ZbbshpqWTlHtTtbxxrOFq0zcpyS92G+NTF6ASS\nhXcIf90du/mBWd2dinF/w2nkRAWfGBy8bGnUSJ93rPVwLjI0PDeHh7+PSQ+3X6mG\n5DI9EmzEC7esW6wJbhgiOYXLavAOmLfI0yq/z8SZMvFYwBE69VuGfPSj/u4nIhA5\nK0Qgnw==\n-----END CERTIFICATE-----\n',
        'b0c86e06345f1b1b8b50696b5b42458699359e7dde13f535d7598db06891ccd7f4558f8262e23d8825cb65d0f16c72e53f93db7aa51b0831365db2dc8bbefc17d2c535646122ee1e448853044eeb83ffa944fac27e461ed41aa0f9d2079f49b60c88413fcedb287886094a831c79979b9323eac8fdabc1447facdd629d5533d6bc3f1a6a4ba4e420b7733b8617fe15f4f7a9ec81c0ae5b312dab6634082b29450bb77c19cda733719ecc8d758ec7988e39ff1f23dc5cf023156a82f1a73aaf2860d19dc64b452b4b15aa651d8845dbef97f07e3021babd5bdab3b353de271f0c3f95c29087f332d912a684560cad91e097a8978f42e8587b6c034e58ebbe1175',
        PKCS1v15_PADDING,
        "did:sov:55GkHamhTU1ZbTbV2ab9DE"
    )

]

paddings = [
    PSS_PADDING,
    PKCS1v15_PADDING
]

all_type_dids = [
    b"\xd6\x98\x04\x88\xd2-\xc1D\x02\x15\xc9Z\x9bK \x8f\xe0\x8b5\xd0Z$",
    "did:sov:55GkHamhTU1ZbTbV2ab9DE",
    0
]

all_type_certificates = [
    b"\xd6\x98\x04\x88\xd2-\xc1D\x02\x15\xc9Z\x9bK \x8f\xe0\x8b5\xd0Z$",
    0,
    ""
]

bad_type_proofs = [
    "this is a proof",
    20
]

service_endpoints = [
    (
        "did:sov:55GkHamhTU1ZbTbV2ab9DE", 
        "http://service_endpoint.sample/did:sov:55GkHamhTU1ZbTbV2ab9DE/eidas"
    ),
    (
        "did:example:21tDAKCERh95uGgKbJNHYp",
        "http://service_endpoint.sample/did:example:21tDAKCERh95uGgKbJNHYp/eidas"
    )
]

bad_type_endpoints = [
    b"\xd6\x98\x04\x88\xd2-\xc1D\x02\x15\xc9Z\x9bK \x8f\xe0\x8b5\xd0Z$",
    0
]

credentials = [
    {
        "@context": [
            "https://www.w3.org/2018/credentials/v1",
            "https://www.w3.org/2018/credentials/examples/v1"
        ],
        "id": "http://example.edu/credentials/3732",
        "type": ["VerifiableCredential", "UniversityDegreeCredential"],
        "issuer": "did:example:123456789abcdefghi",
        "issuanceDate": "2010-01-01T19:23:24Z",
        "credentialSubject": {
            "id": "did:example:ebfeb1f712ebc6f1c276e12ec21",
            "degree": {
                "type": "BachelorDegree",
                "name": "Bachelor of Science and Arts"
                }  
            },
        "proof": {
            "type": "RsaSignature2018",
            "created": "2018-06-18T21:19:10Z",
            "proofPurpose": "assertionMethod",
            "verificationMethod": "https://example.com/jdoe/keys/1",
            "jws": "eyJhbGciOiJQUzI1NiIsImI2NCI6ZmFsc2UsImNyaXQiOlsiYjY0Il19DJBMvvFAIC00nSGB6Tn0XKbbF9XrsaJZREWvR2aONYTQQxnyXirtXnlewJMBBn2h9hfcGZrvnC1b6PgWmukzFJ1IiH1dWgnDIS81BH-IxXnPkbuYDeySorc4QU9MJxdVkY5EL4HYbcIfwKj6X4LBQ2_ZHZIu1jdqLcRZqHcsDF5KKylKc1THn5VRWy5WhYg_gBnyWny8E6Qkrze53MR7OuAmmNJ1m1nN8SxDrG6a08L78J0-Fbas5OjAQz3c17GY8mVuDPOBIOVjMEghBlgl3nOi1ysxbRGhHLEK4s0KKbeRogZdgt1DkQxDFxxn41QWDw_mmMCjs9qxg0zcZzqEJw"
        }
    }
] 

bad_credentials = [
    {
        "@context": [
            "https://www.w3.org/2018/credentials/v1",
            "https://www.w3.org/2018/credentials/examples/v1"
        ],
        "id": "http://example.edu/credentials/3732",
        "type": ["VerifiableCredential", "UniversityDegreeCredential"],
        "credentialSubject": {
            "id": "did:example:ebfeb1f712ebc6f1c276e12ec21",
            "degree": {
                "type": "BachelorDegree",
                "name": "Bachelor of Science and Arts"
                }  
            },
        "proof": {}
    }
] 

bad_type_credentials = [
    b"\xd6\x98\x04\x88\xd2-\xc1D\x02\x15\xc9Z\x9bK \x8f\xe0\x8b5\xd0Z$",
    0
] 

did_documents = [
    {
        "@context": "https://w3id.org/did/v1",
        "id": "did:example:123456789abcdefghi",
        "authentication": [{
            "id": "did:example:123456789abcdefghi#keys-1",
            "type": "RsaVerificationKey2018",
            "controller": "did:example:123456789abcdefghi",
            "publicKeyPem": "-----BEGIN PUBLIC KEY...END PUBLIC KEY-----\r\n"
        }],
        "service": [{
            "id": "did:example:123456789abcdefghi#vc",
            "type": "VerifiableCredentialService",
            "serviceEndpoint": "https://example.com/vc/"
        }, {
            "id": "did:example:21tDAKCERh95uGgKbJNHYp#eidas",
            "type": "EidasService",
            "serviceEndpoint": "http://localhost:8000/did:example:21tDAKCERh95uGgKbJNHYp/eidas"
        }]
    }
]

bad_did_documents = [
    {
        "@context": "https://w3id.org/did/v1",
        "authentication": [{
            "id": "did:example:123456789abcdefghi#keys-1",
            "type": "RsaVerificationKey2018",
            "controller": "did:example:123456789abcdefghi",
            "publicKeyPem": "-----BEGIN PUBLIC KEY...END PUBLIC KEY-----\r\n"
        }],
        "service": [{
            "id": "did:example:123456789abcdefghi#vc",
            "type": "VerifiableCredentialService",
            "serviceEndpoint": "https://example.com/vc/"
        }]
    },
    {
        "@context": "https://w3id.org/did/v1",
        "id": "did:example:123456789abcdefghi",
        "authentication": [{
            "id": "did:example:123456789abcdefghi#keys-1",
            "type": "RsaVerificationKey2018",
            "controller": "did:example:123456789abcdefghi",
            "publicKeyPem": "-----BEGIN PUBLIC KEY...END PUBLIC KEY-----\r\n"
        }],
        "service": [{
            "id": "did:example:123456789abcdefghi#vc",
            "type": "VerifiableCredentialService",
            "serviceEndpoint": "https://example.com/vc/"
        }]
    }
]

bad_obj_type_paddings = [
    b"\xd6\x98\x04\x88\xd2-\xc1D\x02\x15\xc9Z\x9bK \x8f\xe0\x8b5\xd0Z$",
    0
]

bad_type_paddings = [
    "new_padding"
]

crypto_testdata = [
    ("","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
    (" ","36a9e7f1c95b82ffb99743e0c5c4ce95d83c9a430aac59f84ef3cbfab6145068"),
    ("a","ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"),
    ("0","5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9"),
    ("did:sov:", "97b40a411bf0e69968c6a0280c88f0d4f170245522d2d07c0cc39ffeffeb7bb2"),
    ("55GkHamhTU1ZbTbV2ab9DE", "9f4fc75928e784dbe2e5a33500aaa08a11906b02ef38309bf23208dca4452ef8"),
    ("did:sov:55GkHamhTU1ZbTbV2ab9DE","32eaebf15929b44167130a124c73b4652f122b9fc92ef5bde91a32f70c2bf049"),
    ("did:test:abcdefghijkl","eff857db6f037dec456ab0802998313059731f39a3f45b72413af30610f79f8c")
]

eidas_services = [
    {
        "id": "did:sov:55GkHamhTU1ZbTbV2ab9DE#eidas",
        "type": "EidasService",
        "serviceEndpoint": "http://service_endpoint.sample/did:sov:55GkHamhTU1ZbTbV2ab9DE/eidas"
    },
    {
        "id": "did:example:21tDAKCERh95uGgKbJNHYp#eidas",
        "type": "EidasService",
        "serviceEndpoint": "http://service_endpoint.sample/did:example:21tDAKCERh95uGgKbJNHYp/eidas"
    }
]

did_doc_services = [
    {
        "id": "did:example:123456789abcdefghi#openid",
        "type": "OpenIdConnectVersion1.0Service",
        "serviceEndpoint": "https://openid.example.com/"
    }, 
    {
        "id": "did:example:123456789abcdefghi#vcr",
        "type": "CredentialRepositoryService",
        "serviceEndpoint": "https://repository.example.com/service/8377464"
    }, 
    {
        "id": "did:example:123456789abcdefghi#xdi",
        "type": "XdiService",
        "serviceEndpoint": "https://xdi.example.com/8377464"
    }, 
    {
        "id": "did:example:123456789abcdefghi#agent",
        "type": "AgentService",
        "serviceEndpoint": "https://agent.example.com/8377464"
    }, 
    {
        "id": "did:example:123456789abcdefghi#hub",
        "type": "HubService",
        "serviceEndpoint": "https://hub.example.com/.identity/did:example:0123456789abcdef/"
    }, 
    {
        "id": "did:example:123456789abcdefghi#messages",
        "type": "MessagingService",
        "serviceEndpoint": "https://example.com/messages/8377464"
    }, 
    {
        "id": "did:example:123456789abcdefghi#inbox",
        "type": "SocialWebInboxService",
        "serviceEndpoint": "https://social.example.com/83hfh37dj",
        "description": "My public social inbox",
            "spamCost": {
            "amount": "0.50",
            "currency": "USD"
        }
    }, 
    {
        "id": "did:example:123456789abcdefghi#authpush",
        "type": "DidAuthPushModeVersion1",
        "serviceEndpoint": "http://auth.example.com/did:example:123456789abcdefg"
    },
    {
        "id": "did:sov:55GkHamhTU1ZbTbV2ab9DE#eidas",
        "type": "EidasService",
        "serviceEndpoint": "http://service_endpoint.sample/did:sov:55GkHamhTU1ZbTbV2ab9DE/eidas"
    }
]

did_doc_services_no_eidas = [
    {
        "id": "did:example:123456789abcdefghi#openid",
        "type": "OpenIdConnectVersion1.0Service",
        "serviceEndpoint": "https://openid.example.com/"
    }, 
    {
        "id": "did:example:123456789abcdefghi#vcr",
        "type": "CredentialRepositoryService",
        "serviceEndpoint": "https://repository.example.com/service/8377464"
    }
]

eidas_link_and_diddocs_jsons = [
    (
        {
        "@context": "https://w3id.org/did/v1",
        "id": "did:sov:55GkHamhTU1ZbTbV2ab9DE",
        "authentication": [{
            "id": "did:sov:55GkHamhTU1ZbTbV2ab9DE#keys-1",
            "type": "RsaVerificationKey2018",
            "controller": "did:sov:55GkHamhTU1ZbTbV2ab9DE",
            "publicKeyPem": "-----BEGIN PUBLIC KEY...END PUBLIC KEY-----\r\n"
        }],
        "service": [{
            "id": "did:sov:55GkHamhTU1ZbTbV2ab9DE#vc",
            "type": "VerifiableCredentialService",
            "serviceEndpoint": "https://example.com/vc/"
            }, {
                "id": "did:sov:55GkHamhTU1ZbTbV2ab9DE#eidas",
                "type": "EidasService",
                "serviceEndpoint": "http://localhost:8000/did:example:21tDAKCERh95uGgKbJNHYp/eidas"
            }]
        },
        {
        "type": "EidasLink",
        "created": "2019-07-16 17:25:51.360680+00:00",
        "did": "did:sov:55GkHamhTU1ZbTbV2ab9DE",
        "certificate": "-----BEGIN CERTIFICATE-----\nMIIDYDCCAkigAwIBAgIUI63ffVceaNc1kN9O0q/4jSjbkU0wDQYJKoZIhvcNAQEL\nBQAwXTELMAkGA1UEBhMCRVMxEzARBgNVBAgMClRFU1RfU1RBVEUxEjAQBgNVBAcM\nCVRFU1RfQ0lUWTEQMA4GA1UECgwHQ0FfQUNNRTETMBEGA1UEAwwKbXlzaXRlLmNv\nbTAeFw0xOTA3MDkxNDA3MjBaFw0yMDA3MDgxNDA3MjBaMF0xCzAJBgNVBAYTAkVT\nMRMwEQYDVQQIDApURVNUX1NUQVRFMRIwEAYDVQQHDAlURVNUX0NJVFkxEDAOBgNV\nBAoMB0NBX0FDTUUxEzARBgNVBAMMCm15c2l0ZS5jb20wggEiMA0GCSqGSIb3DQEB\nAQUAA4IBDwAwggEKAoIBAQDm6RhyIeFZHn4bGQ/2UQ+aflczCo3Ej04LJXfiIU1Q\nt7xRq3e+uh7nTLffnS7fj/ZZBBREmR/D/SJBTlxv7WQEbscV/pf2LoZLjoC4M4ye\n43lUHRmWsm4J50tu9zcSheqXCRyAK/Ai6RUBy86NKXMFTUp/ONxS0BxJg8GU03Xd\nXGnYzdmZZXGDnublGYq03gD/cZYguS7/HS8v/MckdmjYPTy2syGL9unYkjWn7vig\niaDc2leAM4agKB6PODJSFla15HLoqskKX1SgtLJUHxu/FOo6hYdCt+GxpV1xhl/r\nEf3/SFeTZrJgL11m5ABDli2zAmCn4bjBNnNcXWy5QV0pAgMBAAGjGDAWMBQGA1Ud\nEQQNMAuCCWxvY2FsaG9zdDANBgkqhkiG9w0BAQsFAAOCAQEAYPUn0TzGyn438++1\nV2jMHC653C8tn3vVF5nTT7Td+ihc+KaaNDYsgyY2JpBIMRwlNgoNU0Da3P/9ZDn3\nlFJElUg8WpWPvpXtbS4udqn6UcfT9mFJtkzKg3CK5i50GRCabV9FPbY1bzYtUbY+\nEntXtI2h0dxcgzgOw6pkXFB3O7ZbbshpqWTlHtTtbxxrOFq0zcpyS92G+NTF6ASS\nhXcIf90du/mBWd2dinF/w2nkRAWfGBy8bGnUSJ93rPVwLjI0PDeHh7+PSQ+3X6mG\n5DI9EmzEC7esW6wJbhgiOYXLavAOmLfI0yq/z8SZMvFYwBE69VuGfPSj/u4nIhA5\nK0Qgnw==\n-----END CERTIFICATE-----\n",
        "proof": {
                "type": "RsaSignature2018",
                "padding": "PSS",
                "signatureValue": "4f1bb7069e1508901e83d9dd71043e35fbc8ecf3077625206dd00cf8f12365096cc1cf07822479e571689bc67c50a7d9ca66c43865e490044729af3356e853073073c11e9fa517f7b35748146c1c1101406f66866969ad5915054e3633ab3c247d6b09be909ece6d018ad309b1b34c45b223227d74928278640e0e6a62de0309309e609e8927eb7abd098dfb8a30e8c91fde3ea4fbe804b2967db2c994d303de1e6ac837cfd2a11414ace2bd75148e917b3505f17fabc4805484164a69fdc1d28122e977c1fa4f62b39a601915d8fe0b1bd6e2932db6c8ca3b2bca3ab04f3aebf83d081122d42248dc2a2f292f2c2bfc42244c3118109ab9f001a85cbdd52f71"
            }
        }
    ),
    (
        {
        "@context": "https://w3id.org/did/v1",
        "id": "did:sov:55GkHamhTU1ZbTbV2ab9DE",
        "authentication": [{
            "id": "did:sov:55GkHamhTU1ZbTbV2ab9DE#keys-1",
            "type": "RsaVerificationKey2018",
            "controller": "did:sov:55GkHamhTU1ZbTbV2ab9DE",
            "publicKeyPem": "-----BEGIN PUBLIC KEY...END PUBLIC KEY-----\r\n"
        }],
        "service": [{
            "id": "did:sov:55GkHamhTU1ZbTbV2ab9DE#vc",
            "type": "VerifiableCredentialService",
            "serviceEndpoint": "https://example.com/vc/"
            }, {
                "id": "did:sov:55GkHamhTU1ZbTbV2ab9DE#eidas",
                "type": "EidasService",
                "serviceEndpoint": "http://localhost:8000/did:example:21tDAKCERh95uGgKbJNHYp/eidas"
            }]
        },
        {
        "type": "EidasLink",
        "created": "2019-07-16 17:25:51.361800+00:00",
        "did": "did:sov:55GkHamhTU1ZbTbV2ab9DE",
        "certificate": "-----BEGIN CERTIFICATE-----\nMIIDYDCCAkigAwIBAgIUI63ffVceaNc1kN9O0q/4jSjbkU0wDQYJKoZIhvcNAQEL\nBQAwXTELMAkGA1UEBhMCRVMxEzARBgNVBAgMClRFU1RfU1RBVEUxEjAQBgNVBAcM\nCVRFU1RfQ0lUWTEQMA4GA1UECgwHQ0FfQUNNRTETMBEGA1UEAwwKbXlzaXRlLmNv\nbTAeFw0xOTA3MDkxNDA3MjBaFw0yMDA3MDgxNDA3MjBaMF0xCzAJBgNVBAYTAkVT\nMRMwEQYDVQQIDApURVNUX1NUQVRFMRIwEAYDVQQHDAlURVNUX0NJVFkxEDAOBgNV\nBAoMB0NBX0FDTUUxEzARBgNVBAMMCm15c2l0ZS5jb20wggEiMA0GCSqGSIb3DQEB\nAQUAA4IBDwAwggEKAoIBAQDm6RhyIeFZHn4bGQ/2UQ+aflczCo3Ej04LJXfiIU1Q\nt7xRq3e+uh7nTLffnS7fj/ZZBBREmR/D/SJBTlxv7WQEbscV/pf2LoZLjoC4M4ye\n43lUHRmWsm4J50tu9zcSheqXCRyAK/Ai6RUBy86NKXMFTUp/ONxS0BxJg8GU03Xd\nXGnYzdmZZXGDnublGYq03gD/cZYguS7/HS8v/MckdmjYPTy2syGL9unYkjWn7vig\niaDc2leAM4agKB6PODJSFla15HLoqskKX1SgtLJUHxu/FOo6hYdCt+GxpV1xhl/r\nEf3/SFeTZrJgL11m5ABDli2zAmCn4bjBNnNcXWy5QV0pAgMBAAGjGDAWMBQGA1Ud\nEQQNMAuCCWxvY2FsaG9zdDANBgkqhkiG9w0BAQsFAAOCAQEAYPUn0TzGyn438++1\nV2jMHC653C8tn3vVF5nTT7Td+ihc+KaaNDYsgyY2JpBIMRwlNgoNU0Da3P/9ZDn3\nlFJElUg8WpWPvpXtbS4udqn6UcfT9mFJtkzKg3CK5i50GRCabV9FPbY1bzYtUbY+\nEntXtI2h0dxcgzgOw6pkXFB3O7ZbbshpqWTlHtTtbxxrOFq0zcpyS92G+NTF6ASS\nhXcIf90du/mBWd2dinF/w2nkRAWfGBy8bGnUSJ93rPVwLjI0PDeHh7+PSQ+3X6mG\n5DI9EmzEC7esW6wJbhgiOYXLavAOmLfI0yq/z8SZMvFYwBE69VuGfPSj/u4nIhA5\nK0Qgnw==\n-----END CERTIFICATE-----\n",
        "proof": {
                "type": "RsaSignature2018",
                "padding": "PKCS1-v1_5",
                "signatureValue": "b0c86e06345f1b1b8b50696b5b42458699359e7dde13f535d7598db06891ccd7f4558f8262e23d8825cb65d0f16c72e53f93db7aa51b0831365db2dc8bbefc17d2c535646122ee1e448853044eeb83ffa944fac27e461ed41aa0f9d2079f49b60c88413fcedb287886094a831c79979b9323eac8fdabc1447facdd629d5533d6bc3f1a6a4ba4e420b7733b8617fe15f4f7a9ec81c0ae5b312dab6634082b29450bb77c19cda733719ecc8d758ec7988e39ff1f23dc5cf023156a82f1a73aaf2860d19dc64b452b4b15aa651d8845dbef97f07e3021babd5bdab3b353de271f0c3f95c29087f332d912a684560cad91e097a8978f42e8587b6c034e58ebbe1175"
            }
        }
    )
]