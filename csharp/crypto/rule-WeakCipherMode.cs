// License: MIT Copyright (c) 2022-Present GitLab B.V.
using System.Security.Cryptography;

class WeakCipherMode
{
  public static readonly int BlockBitSize = 128;
  public static readonly int KeyBitSize = 256;

  static void WeakCipher()
  {
    new AesManaged
    {
      KeySize = KeyBitSize,
      BlockSize = BlockBitSize,
      // ruleid: csharp_crypto_rule-WeakCipherMode
      Mode = CipherMode.OFB,
      Padding = PaddingMode.PKCS7
    };

    var des = DES.Create();

    // ruleid: csharp_crypto_rule-WeakCipherMode
    des.Mode = CipherMode.CTS;
  }
}
