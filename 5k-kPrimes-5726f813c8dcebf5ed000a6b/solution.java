import java.util.ArrayList;
import java.util.List;

public class KPrimes {

    public static long findPrimeNumbers(long endOfRange) {
        List<Long> longs = new ArrayList<>();
        long i = 2;
        while (i * i <= endOfRange) {
            while (endOfRange % i == 0) {
                longs.add(i);
                endOfRange /= i;
            }
            i++;
        }
        if (endOfRange > 1) {
            longs.add(endOfRange);
        }
        return longs.size();
    }

    public static long[] countKprimes(long k, long start, long end) {
        List<Long> longs = new ArrayList<>();
        long i = start;
        while (i <= end) {
            if (findPrimeNumbers(i) == k) {
                longs.add(i);
            }
            i++;
        }
        return longs.stream().mapToLong(x -> x).toArray();
    }

    public static int puzzle(int s) {
        long[] aPrimes = countKprimes(1, 0, s );
        long[] bPrimes = countKprimes(3, 0, s );
        long[] cPrimes = countKprimes(7, 0, s );
        int resultCount = 0;
        int ia = 0;
        while(ia < aPrimes.length) {
            int ib = 0;
            while(ib < bPrimes.length) {
                int ic = 0;
                while(ic <cPrimes.length) {
                    if(aPrimes[ia] + bPrimes[ib] + cPrimes[ic] == s) {
                        resultCount++;
                    }
                    ic++;
                }
                ib++;
            }
            ia++;
        }
        return resultCount;
    }
}
