"""
Test keys and data for self-test operations.

Test data from:
NIST SP 800-38A http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf
NIST FIPS-197 http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf

Copyright (c) 2010, Adam Newman http://www.caller9.com/
Licensed under the MIT license http://www.opensource.org/licenses/mit-license.php
"""
__author__ = "Adam Newman"


class TestKeys:
    """Test data, keys, IVs, and output to use in self-tests"""

    test_key = {
        128: [
            0x00,
            0x01,
            0x02,
            0x03,
            0x04,
            0x05,
            0x06,
            0x07,
            0x08,
            0x09,
            0x0A,
            0x0B,
            0x0C,
            0x0D,
            0x0E,
            0x0F,
        ],
        192: [
            0x00,
            0x01,
            0x02,
            0x03,
            0x04,
            0x05,
            0x06,
            0x07,
            0x08,
            0x09,
            0x0A,
            0x0B,
            0x0C,
            0x0D,
            0x0E,
            0x0F,
            0x10,
            0x11,
            0x12,
            0x13,
            0x14,
            0x15,
            0x16,
            0x17,
        ],
        256: [
            0x00,
            0x01,
            0x02,
            0x03,
            0x04,
            0x05,
            0x06,
            0x07,
            0x08,
            0x09,
            0x0A,
            0x0B,
            0x0C,
            0x0D,
            0x0E,
            0x0F,
            0x10,
            0x11,
            0x12,
            0x13,
            0x14,
            0x15,
            0x16,
            0x17,
            0x18,
            0x19,
            0x1A,
            0x1B,
            0x1C,
            0x1D,
            0x1E,
            0x1F,
        ],
    }

    test_expanded_key_validated = {
        128: [
            0x00,
            0x01,
            0x02,
            0x03,
            0x04,
            0x05,
            0x06,
            0x07,
            0x08,
            0x09,
            0x0A,
            0x0B,
            0x0C,
            0x0D,
            0x0E,
            0x0F,
            0xD6,
            0xAA,
            0x74,
            0xFD,
            0xD2,
            0xAF,
            0x72,
            0xFA,
            0xDA,
            0xA6,
            0x78,
            0xF1,
            0xD6,
            0xAB,
            0x76,
            0xFE,
            0xB6,
            0x92,
            0xCF,
            0x0B,
            0x64,
            0x3D,
            0xBD,
            0xF1,
            0xBE,
            0x9B,
            0xC5,
            0x00,
            0x68,
            0x30,
            0xB3,
            0xFE,
            0xB6,
            0xFF,
            0x74,
            0x4E,
            0xD2,
            0xC2,
            0xC9,
            0xBF,
            0x6C,
            0x59,
            0x0C,
            0xBF,
            0x04,
            0x69,
            0xBF,
            0x41,
            0x47,
            0xF7,
            0xF7,
            0xBC,
            0x95,
            0x35,
            0x3E,
            0x03,
            0xF9,
            0x6C,
            0x32,
            0xBC,
            0xFD,
            0x05,
            0x8D,
            0xFD,
            0x3C,
            0xAA,
            0xA3,
            0xE8,
            0xA9,
            0x9F,
            0x9D,
            0xEB,
            0x50,
            0xF3,
            0xAF,
            0x57,
            0xAD,
            0xF6,
            0x22,
            0xAA,
            0x5E,
            0x39,
            0x0F,
            0x7D,
            0xF7,
            0xA6,
            0x92,
            0x96,
            0xA7,
            0x55,
            0x3D,
            0xC1,
            0x0A,
            0xA3,
            0x1F,
            0x6B,
            0x14,
            0xF9,
            0x70,
            0x1A,
            0xE3,
            0x5F,
            0xE2,
            0x8C,
            0x44,
            0x0A,
            0xDF,
            0x4D,
            0x4E,
            0xA9,
            0xC0,
            0x26,
            0x47,
            0x43,
            0x87,
            0x35,
            0xA4,
            0x1C,
            0x65,
            0xB9,
            0xE0,
            0x16,
            0xBA,
            0xF4,
            0xAE,
            0xBF,
            0x7A,
            0xD2,
            0x54,
            0x99,
            0x32,
            0xD1,
            0xF0,
            0x85,
            0x57,
            0x68,
            0x10,
            0x93,
            0xED,
            0x9C,
            0xBE,
            0x2C,
            0x97,
            0x4E,
            0x13,
            0x11,
            0x1D,
            0x7F,
            0xE3,
            0x94,
            0x4A,
            0x17,
            0xF3,
            0x07,
            0xA7,
            0x8B,
            0x4D,
            0x2B,
            0x30,
            0xC5,
        ],
        192: [
            0x00,
            0x01,
            0x02,
            0x03,
            0x04,
            0x05,
            0x06,
            0x07,
            0x08,
            0x09,
            0x0A,
            0x0B,
            0x0C,
            0x0D,
            0x0E,
            0x0F,
            0x10,
            0x11,
            0x12,
            0x13,
            0x14,
            0x15,
            0x16,
            0x17,
            0x58,
            0x46,
            0xF2,
            0xF9,
            0x5C,
            0x43,
            0xF4,
            0xFE,
            0x54,
            0x4A,
            0xFE,
            0xF5,
            0x58,
            0x47,
            0xF0,
            0xFA,
            0x48,
            0x56,
            0xE2,
            0xE9,
            0x5C,
            0x43,
            0xF4,
            0xFE,
            0x40,
            0xF9,
            0x49,
            0xB3,
            0x1C,
            0xBA,
            0xBD,
            0x4D,
            0x48,
            0xF0,
            0x43,
            0xB8,
            0x10,
            0xB7,
            0xB3,
            0x42,
            0x58,
            0xE1,
            0x51,
            0xAB,
            0x04,
            0xA2,
            0xA5,
            0x55,
            0x7E,
            0xFF,
            0xB5,
            0x41,
            0x62,
            0x45,
            0x08,
            0x0C,
            0x2A,
            0xB5,
            0x4B,
            0xB4,
            0x3A,
            0x02,
            0xF8,
            0xF6,
            0x62,
            0xE3,
            0xA9,
            0x5D,
            0x66,
            0x41,
            0x0C,
            0x08,
            0xF5,
            0x01,
            0x85,
            0x72,
            0x97,
            0x44,
            0x8D,
            0x7E,
            0xBD,
            0xF1,
            0xC6,
            0xCA,
            0x87,
            0xF3,
            0x3E,
            0x3C,
            0xE5,
            0x10,
            0x97,
            0x61,
            0x83,
            0x51,
            0x9B,
            0x69,
            0x34,
            0x15,
            0x7C,
            0x9E,
            0xA3,
            0x51,
            0xF1,
            0xE0,
            0x1E,
            0xA0,
            0x37,
            0x2A,
            0x99,
            0x53,
            0x09,
            0x16,
            0x7C,
            0x43,
            0x9E,
            0x77,
            0xFF,
            0x12,
            0x05,
            0x1E,
            0xDD,
            0x7E,
            0x0E,
            0x88,
            0x7E,
            0x2F,
            0xFF,
            0x68,
            0x60,
            0x8F,
            0xC8,
            0x42,
            0xF9,
            0xDC,
            0xC1,
            0x54,
            0x85,
            0x9F,
            0x5F,
            0x23,
            0x7A,
            0x8D,
            0x5A,
            0x3D,
            0xC0,
            0xC0,
            0x29,
            0x52,
            0xBE,
            0xEF,
            0xD6,
            0x3A,
            0xDE,
            0x60,
            0x1E,
            0x78,
            0x27,
            0xBC,
            0xDF,
            0x2C,
            0xA2,
            0x23,
            0x80,
            0x0F,
            0xD8,
            0xAE,
            0xDA,
            0x32,
            0xA4,
            0x97,
            0x0A,
            0x33,
            0x1A,
            0x78,
            0xDC,
            0x09,
            0xC4,
            0x18,
            0xC2,
            0x71,
            0xE3,
            0xA4,
            0x1D,
            0x5D,
        ],
        256: [
            0x00,
            0x01,
            0x02,
            0x03,
            0x04,
            0x05,
            0x06,
            0x07,
            0x08,
            0x09,
            0x0A,
            0x0B,
            0x0C,
            0x0D,
            0x0E,
            0x0F,
            0x10,
            0x11,
            0x12,
            0x13,
            0x14,
            0x15,
            0x16,
            0x17,
            0x18,
            0x19,
            0x1A,
            0x1B,
            0x1C,
            0x1D,
            0x1E,
            0x1F,
            0xA5,
            0x73,
            0xC2,
            0x9F,
            0xA1,
            0x76,
            0xC4,
            0x98,
            0xA9,
            0x7F,
            0xCE,
            0x93,
            0xA5,
            0x72,
            0xC0,
            0x9C,
            0x16,
            0x51,
            0xA8,
            0xCD,
            0x02,
            0x44,
            0xBE,
            0xDA,
            0x1A,
            0x5D,
            0xA4,
            0xC1,
            0x06,
            0x40,
            0xBA,
            0xDE,
            0xAE,
            0x87,
            0xDF,
            0xF0,
            0x0F,
            0xF1,
            0x1B,
            0x68,
            0xA6,
            0x8E,
            0xD5,
            0xFB,
            0x03,
            0xFC,
            0x15,
            0x67,
            0x6D,
            0xE1,
            0xF1,
            0x48,
            0x6F,
            0xA5,
            0x4F,
            0x92,
            0x75,
            0xF8,
            0xEB,
            0x53,
            0x73,
            0xB8,
            0x51,
            0x8D,
            0xC6,
            0x56,
            0x82,
            0x7F,
            0xC9,
            0xA7,
            0x99,
            0x17,
            0x6F,
            0x29,
            0x4C,
            0xEC,
            0x6C,
            0xD5,
            0x59,
            0x8B,
            0x3D,
            0xE2,
            0x3A,
            0x75,
            0x52,
            0x47,
            0x75,
            0xE7,
            0x27,
            0xBF,
            0x9E,
            0xB4,
            0x54,
            0x07,
            0xCF,
            0x39,
            0x0B,
            0xDC,
            0x90,
            0x5F,
            0xC2,
            0x7B,
            0x09,
            0x48,
            0xAD,
            0x52,
            0x45,
            0xA4,
            0xC1,
            0x87,
            0x1C,
            0x2F,
            0x45,
            0xF5,
            0xA6,
            0x60,
            0x17,
            0xB2,
            0xD3,
            0x87,
            0x30,
            0x0D,
            0x4D,
            0x33,
            0x64,
            0x0A,
            0x82,
            0x0A,
            0x7C,
            0xCF,
            0xF7,
            0x1C,
            0xBE,
            0xB4,
            0xFE,
            0x54,
            0x13,
            0xE6,
            0xBB,
            0xF0,
            0xD2,
            0x61,
            0xA7,
            0xDF,
            0xF0,
            0x1A,
            0xFA,
            0xFE,
            0xE7,
            0xA8,
            0x29,
            0x79,
            0xD7,
            0xA5,
            0x64,
            0x4A,
            0xB3,
            0xAF,
            0xE6,
            0x40,
            0x25,
            0x41,
            0xFE,
            0x71,
            0x9B,
            0xF5,
            0x00,
            0x25,
            0x88,
            0x13,
            0xBB,
            0xD5,
            0x5A,
            0x72,
            0x1C,
            0x0A,
            0x4E,
            0x5A,
            0x66,
            0x99,
            0xA9,
            0xF2,
            0x4F,
            0xE0,
            0x7E,
            0x57,
            0x2B,
            0xAA,
            0xCD,
            0xF8,
            0xCD,
            0xEA,
            0x24,
            0xFC,
            0x79,
            0xCC,
            0xBF,
            0x09,
            0x79,
            0xE9,
            0x37,
            0x1A,
            0xC2,
            0x3C,
            0x6D,
            0x68,
            0xDE,
            0x36,
        ],
    }

    test_block_ciphertext_validated = {
        128: [
            0x69,
            0xC4,
            0xE0,
            0xD8,
            0x6A,
            0x7B,
            0x04,
            0x30,
            0xD8,
            0xCD,
            0xB7,
            0x80,
            0x70,
            0xB4,
            0xC5,
            0x5A,
        ],
        192: [
            0xDD,
            0xA9,
            0x7C,
            0xA4,
            0x86,
            0x4C,
            0xDF,
            0xE0,
            0x6E,
            0xAF,
            0x70,
            0xA0,
            0xEC,
            0x0D,
            0x71,
            0x91,
        ],
        256: [
            0x8E,
            0xA2,
            0xB7,
            0xCA,
            0x51,
            0x67,
            0x45,
            0xBF,
            0xEA,
            0xFC,
            0x49,
            0x90,
            0x4B,
            0x49,
            0x60,
            0x89,
        ],
    }

    test_block_plaintext = [
        0x00,
        0x11,
        0x22,
        0x33,
        0x44,
        0x55,
        0x66,
        0x77,
        0x88,
        0x99,
        0xAA,
        0xBB,
        0xCC,
        0xDD,
        0xEE,
        0xFF,
    ]

    # After initial validation, these deviated from test in SP 800-38A to use same key, iv, and plaintext on tests.
    # Still valid, just easier to test with.
    test_mode_key = [
        0x60,
        0x3D,
        0xEB,
        0x10,
        0x15,
        0xCA,
        0x71,
        0xBE,
        0x2B,
        0x73,
        0xAE,
        0xF0,
        0x85,
        0x7D,
        0x77,
        0x81,
        0x1F,
        0x35,
        0x2C,
        0x07,
        0x3B,
        0x61,
        0x08,
        0xD7,
        0x2D,
        0x98,
        0x10,
        0xA3,
        0x09,
        0x14,
        0xDF,
        0xF4,
    ]
    test_mode_iv = [
        0x00,
        0x01,
        0x02,
        0x03,
        0x04,
        0x05,
        0x06,
        0x07,
        0x08,
        0x09,
        0x0A,
        0x0B,
        0x0C,
        0x0D,
        0x0E,
        0x0F,
    ]
    test_mode_plaintext = [
        [
            0x6B,
            0xC1,
            0xBE,
            0xE2,
            0x2E,
            0x40,
            0x9F,
            0x96,
            0xE9,
            0x3D,
            0x7E,
            0x11,
            0x73,
            0x93,
            0x17,
            0x2A,
        ],
        [
            0xAE,
            0x2D,
            0x8A,
            0x57,
            0x1E,
            0x03,
            0xAC,
            0x9C,
            0x9E,
            0xB7,
            0x6F,
            0xAC,
            0x45,
            0xAF,
            0x8E,
            0x51,
        ],
        [
            0x30,
            0xC8,
            0x1C,
            0x46,
            0xA3,
            0x5C,
            0xE4,
            0x11,
            0xE5,
            0xFB,
            0xC1,
            0x19,
            0x1A,
            0x0A,
            0x52,
            0xEF,
        ],
        [
            0xF6,
            0x9F,
            0x24,
            0x45,
            0xDF,
            0x4F,
            0x9B,
            0x17,
            0xAD,
            0x2B,
            0x41,
            0x7B,
            0xE6,
            0x6C,
            0x37,
            0x10,
        ],
    ]
    test_cbc_ciphertext = [
        [
            0xF5,
            0x8C,
            0x4C,
            0x04,
            0xD6,
            0xE5,
            0xF1,
            0xBA,
            0x77,
            0x9E,
            0xAB,
            0xFB,
            0x5F,
            0x7B,
            0xFB,
            0xD6,
        ],
        [
            0x9C,
            0xFC,
            0x4E,
            0x96,
            0x7E,
            0xDB,
            0x80,
            0x8D,
            0x67,
            0x9F,
            0x77,
            0x7B,
            0xC6,
            0x70,
            0x2C,
            0x7D,
        ],
        [
            0x39,
            0xF2,
            0x33,
            0x69,
            0xA9,
            0xD9,
            0xBA,
            0xCF,
            0xA5,
            0x30,
            0xE2,
            0x63,
            0x04,
            0x23,
            0x14,
            0x61,
        ],
        [
            0xB2,
            0xEB,
            0x05,
            0xE2,
            0xC3,
            0x9B,
            0xE9,
            0xFC,
            0xDA,
            0x6C,
            0x19,
            0x07,
            0x8C,
            0x6A,
            0x9D,
            0x1B,
        ],
    ]
    test_cfb_ciphertext = [
        [
            0xDC,
            0x7E,
            0x84,
            0xBF,
            0xDA,
            0x79,
            0x16,
            0x4B,
            0x7E,
            0xCD,
            0x84,
            0x86,
            0x98,
            0x5D,
            0x38,
            0x60,
        ],
        [
            0x39,
            0xFF,
            0xED,
            0x14,
            0x3B,
            0x28,
            0xB1,
            0xC8,
            0x32,
            0x11,
            0x3C,
            0x63,
            0x31,
            0xE5,
            0x40,
            0x7B,
        ],
        [
            0xDF,
            0x10,
            0x13,
            0x24,
            0x15,
            0xE5,
            0x4B,
            0x92,
            0xA1,
            0x3E,
            0xD0,
            0xA8,
            0x26,
            0x7A,
            0xE2,
            0xF9,
        ],
        [
            0x75,
            0xA3,
            0x85,
            0x74,
            0x1A,
            0xB9,
            0xCE,
            0xF8,
            0x20,
            0x31,
            0x62,
            0x3D,
            0x55,
            0xB1,
            0xE4,
            0x71,
        ],
    ]
    test_ofb_ciphertext = [
        [
            0xDC,
            0x7E,
            0x84,
            0xBF,
            0xDA,
            0x79,
            0x16,
            0x4B,
            0x7E,
            0xCD,
            0x84,
            0x86,
            0x98,
            0x5D,
            0x38,
            0x60,
        ],
        [
            0x4F,
            0xEB,
            0xDC,
            0x67,
            0x40,
            0xD2,
            0x0B,
            0x3A,
            0xC8,
            0x8F,
            0x6A,
            0xD8,
            0x2A,
            0x4F,
            0xB0,
            0x8D,
        ],
        [
            0x71,
            0xAB,
            0x47,
            0xA0,
            0x86,
            0xE8,
            0x6E,
            0xED,
            0xF3,
            0x9D,
            0x1C,
            0x5B,
            0xBA,
            0x97,
            0xC4,
            0x08,
        ],
        [
            0x01,
            0x26,
            0x14,
            0x1D,
            0x67,
            0xF3,
            0x7B,
            0xE8,
            0x53,
            0x8F,
            0x5A,
            0x8B,
            0xE7,
            0x40,
            0xE4,
            0x84,
        ],
    ]

    def hex_output(self, list):
        # Debugging output helper
        result = "["
        for i in list[:-1]:
            result += hex(i) + ","
        return result + hex(list[-1]) + "]"
