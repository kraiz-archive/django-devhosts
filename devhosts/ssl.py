import OpenSSL


dump_key = lambda key: OpenSSL.crypto.dump_privatekey(
    OpenSSL.crypto.FILETYPE_PEM,
    key)
load_key = lambda key: OpenSSL.crypto.load_privatekey(
    OpenSSL.crypto.FILETYPE_PEM,
    key)

dump_cert = lambda cert: OpenSSL.crypto.dump_certificate(
    OpenSSL.crypto.FILETYPE_PEM,
    cert)
load_cert = lambda cert: OpenSSL.crypto.load_certificate(
    OpenSSL.crypto.FILETYPE_PEM,
    cert)

def create_key(bits=2048):
    key = OpenSSL.crypto.PKey()
    key.generate_key(OpenSSL.crypto.TYPE_RSA, bits)
    return key


def create_ca_cert(key, domain, days_valid=3650):
    ca = OpenSSL.crypto.X509()
    ca.set_version(3)
    ca.set_serial_number(1)
    ca.get_subject().CN = domain
    ca.gmtime_adj_notBefore(0)
    ca.gmtime_adj_notAfter(days_valid * 60 * 60)
    ca.set_issuer(ca.get_subject())
    ca.set_pubkey(key)
    ca.add_extensions([
        OpenSSL.crypto.X509Extension(
            b'basicConstraints',
            True,
            b'CA:TRUE, pathlen:0'),
        OpenSSL.crypto.X509Extension(
            b'keyUsage',
            True,
            b'keyCertSign, cRLSign'),
        OpenSSL.crypto.X509Extension(
            b'subjectKeyIdentifier',
            False,
            b'hash',
            subject=ca),
    ])
    ca.sign(key, 'sha1')
    return ca


def create_signed_cert(key, domain, ca_key, ca_cert, days_valid=3650):
    cert = OpenSSL.crypto.X509()
    cert.get_subject().CN = domain
    cert.set_serial_number(1)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(days_valid * 60 * 60)
    cert.set_issuer(ca_cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(ca_key, 'sha1')
    return cert
