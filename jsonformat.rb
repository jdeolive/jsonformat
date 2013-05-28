require 'formula'

class Jsonformat < Formula
  homepage 'https://github.com/jdeolive/jsonformat'
  url 'https://github.com/jdeolive/jsonformat/archive/v1.0.tar.gz'
  sha1 '9335328aecfb0fecd973ebf86aa807162e1db8c0'

  def install
    bin.install "jsonformat.py" => "jsonformat"
  end

end
