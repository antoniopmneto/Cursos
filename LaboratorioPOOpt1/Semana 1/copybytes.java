public class CopyBytes {
    public static void main(String[] args) throws IOException {

        FileInputStream in = null;
        FileInputStream out = null;

        try {
            in = new FileInputStream("arquivo.txt");
            out = new FileOutputStream("arquivoout.txt");

            int c;

            while ((c = in.read()) != -1) {
                out.write(c);
            }
        
        } finally {
            if (in != null) {
                in.close();
            }

            if (out != null) {
                out.close();
            }
        }
    } 
}

// Lê byte a byte de um arquivo e transfere para outro arquivo