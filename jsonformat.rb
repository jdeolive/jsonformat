require 'formula'

class Jsonformat < Formula
  homepage 'https://github.com/jdeolive/jsonformat'
  url 'https://github.com/jdeolive/jsonformat/archive/v1.1.tar.gz'
  sha1 'b7ab521cc81f5c538bcd39873fa9d8ff98aa6dde'

  def install
    bin.install "jsonformat.py" => "jsonformat"
  end

end
