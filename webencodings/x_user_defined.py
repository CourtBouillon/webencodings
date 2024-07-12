"""

    webencodings.x_user_defined
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    An implementation of the x-user-defined encoding.

    :copyright: Copyright 2012 by Simon Sapin
    :license: BSD, see LICENSE for details.

"""

import codecs


### Codec APIs

class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table)


class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


### encodings module API

codec_info = codecs.CodecInfo(
    name='x-user-defined',
    encode=Codec().encode,
    decode=Codec().decode,
    incrementalencoder=IncrementalEncoder,
    incrementaldecoder=IncrementalDecoder,
    streamreader=StreamReader,
    streamwriter=StreamWriter,
)


### Decoding Table

decoding_table = ''.join(chr(c if c < 128 else c + 0xF700) for c in range(256))


### Encoding table

encoding_table = codecs.charmap_build(decoding_table)
