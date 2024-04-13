import java.util.Random;

public class RandomSequenceGenerator {
    /**
     * the function that generates a pseudo-random sequence
     * 
     * @param number_bits length of required sequence
     */
    public static void main(String[] args) {
        int len = 128;
        int minDigit = 0;
        int maxDigit = 1;
        String sequence = generateRandomSequence(len, minDigit, maxDigit);
        System.out.println(sequence);
    }

    public static String generateRandomSequence(int len, int minDigit, int maxDigit) {
        Random random = new Random();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < len; i++) {
            int randomDigit = random.nextInt(maxDigit - minDigit + 1) + minDigit;
            sb.append(randomDigit);
        }
        return sb.toString();
    }
}