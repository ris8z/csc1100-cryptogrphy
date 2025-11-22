/*
 * author: Giuseppe Esposito
 * student id: 22702705
 * date: 22/11/2025
 *
 * Everything in this file is considered my own work with the except of the following resources:
 *  
 * [1] baeldung, “SHA-256 Hashing in Java | Baeldung,” Baeldung, May 07, 2019. https://www.baeldung.com/sha-256-hashing-java ‌
 * [2] “HexFormat (Java SE 17 & JDK 17),” Oracle.com, 2025. https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HexFormat.html  ‌ 
 * [3] “Formatter (Java Platform SE 8 ),” Oracle.com, Jun. 30, 2025. https://docs.oracle.com/javase/8/docs/api/java/util/Formatter.html#syntax ‌
 * [4] “BigInteger (Java Platform SE 8 ),” docs.oracle.com. https://docs.oracle.com/javase/8/docs/api/java/math/BigInteger.html
 * 
 * */

import java.math.BigInteger;
import java.util.HexFormat;
import java.util.Random;
import java.security.MessageDigest;
import java.nio.file.Files;
import java.nio.file.Paths;


class Assignment2
{ 
    public static void main() throws Exception
    {
        // generate private and public key x, y
        PrimeModules p = new PrimeModules("""
            b59dd795 68817b4b 9f678982 2d22594f 376e6a9a bc024184 6de426e5 dd8f6edd
            ef00b465 f38f509b 2b183510 64704fe7 5f012fa3 46c5e2c4 42d7c99e ac79b2bc
            8a202c98 327b9681 6cb80426 98ed3734 643c4c05 164e739c b72fba24 f6156b6f
            47a7300e f778c378 ea301e11 41a6b25d 48f19242 68c62ee8 dd313474 5cdf7323
        """);

        Generator g = new Generator("""
            44ec9d52 c8f9189e 49cd7c70 253c2eb3 154dd4f0 8467a64a 0267c9de fe4119f2
            e373388c fa350a4e 66e432d6 38ccdc58 eb703e31 d4c84e50 398f9f91 677e8864
            1a2d2f61 57e2f4ec 538088dc f5940b05 3c622e53 bab0b4e8 4b1465f5 738f5496
            64bd7430 961d3e5a 2e7bceb6 2418db74 7386a58f f267a993 9833beef b7a6fd68
        """);

        SecretKey x = new SecretKey(p);
        PublicKey y = new PublicKey(g, p, x);

        // get the message m
        Message m = new Message("Assignment2.class"); 

        // Compute the Signed Message (r||s)
        RandomValue k;
        R r;
        S s; 

        do
        {
            k = new RandomValue(p);
            r = new R(g, k, p);
            s = new S(m, x, r, k, p); 
        }
        while(s.value.equals(BigInteger.ZERO));


        // Create/update y.txt, r.txt, s.txt
        Utils.printAsHexInFile(y.value, "y.txt");
        Utils.printAsHexInFile(r.value, "r.txt");
        Utils.printAsHexInFile(s.value, "s.txt");
    }
}

class Utils
{
    static BigInteger generateRandom(BigInteger start, BigInteger end)
    {
        start = start.add(BigInteger.ONE);
        end = end.subtract(BigInteger.ONE);

        if (start.compareTo(end) >= 0) 
            System.exit(1);

        var range = end.subtract(start).add(BigInteger.ONE);
        var random = new BigInteger(range.bitLength(), new Random());

        return random.mod(range).add(start);
    }

    static BigInteger gcd(BigInteger x, BigInteger m)
    {
        var a = x.max(m);
        var b = x.min(m);

        while(!b.equals(BigInteger.ZERO))
        {
            var r = a.mod(b);
            a = b;
            b = r;
        }

        return a;
    }   

    static BigInteger egcd(BigInteger x, BigInteger m)
    {
        var a = m;      
        var b = x;
        var t1 = BigInteger.ZERO;
        var t2 = BigInteger.ONE;

        while(!b.equals(BigInteger.ZERO))
        {
            var q = a.divide(b);
            var r = a.mod(b);
            var t = t1.subtract(t2.multiply(q));

            a = b;
            b = r;
            t1 = t2;
            t2 = t;
        }

        if (!a.equals(BigInteger.ONE)) 
            System.exit(1);

        return t1.mod(m);
    }

    static BigInteger sha256(byte[] data) throws Exception
    {
        var md = MessageDigest.getInstance("SHA-256");
        var hashedBytes= md.digest(data);
        return new BigInteger(1, hashedBytes);
    }

    static void printAsHexInFile(BigInteger output, String fileName) throws Exception
    {
        Files.writeString(Paths.get(fileName), output.toString(16));
    }
}

class S
{
    BigInteger value;
    S(Message m, SecretKey x, R r, RandomValue k,  PrimeModules p) throws Exception
    {
        var H_m = Utils.sha256(m.bytes);
        var P_m1 = p.value.subtract(BigInteger.ONE);
        var K_inv = Utils.egcd(k.value, P_m1);
        this.value = ( H_m.subtract( x.value.multiply(r.value) ) ).multiply( K_inv ).mod( P_m1 );
    }
}

class R 
{
    BigInteger value;

    R (Generator g, RandomValue k,PrimeModules p)
    {
        this.value = g.value.modPow(k.value, p.value);
    }
}

class RandomValue
{
    BigInteger value;

    RandomValue(PrimeModules p) // 1 < k < p - 1  and gcd(k, p - 1) = 1
    { 
        var P_m1 = p.value.subtract(BigInteger.ONE);
        do
        {
            this.value = Utils.generateRandom(BigInteger.ONE, P_m1);
        }
        while (! Utils.gcd(this.value, P_m1).equals(BigInteger.ONE) );
    }
}

class Message
{
    byte[] bytes;
    Message(String fileName) throws Exception
    {
        this.bytes = Files.readAllBytes(Paths.get(fileName));
    }
}

class PublicKey
{
    BigInteger value;
    PublicKey(Generator g, PrimeModules p, SecretKey x)
    {
        this.value = g.value.modPow(x.value, p.value);
    }
}

class SecretKey
{
    BigInteger value;

    SecretKey(PrimeModules p) // 0 < x < p - 1
    { 
        this.value = Utils.generateRandom(BigInteger.ZERO, p.value.subtract(BigInteger.ONE));
    }
}

class Generator 
{
    BigInteger value;

    Generator(String s)
    {
        this.value = new BigInteger(1, HexFormat.of().parseHex(s.replaceAll("\\s+", "")));
    }
}

class PrimeModules 
{
    BigInteger value;

    PrimeModules(String s)
    {
        this.value = new BigInteger(1, HexFormat.of().parseHex(s.replaceAll("\\s+", "")));
    }
}
