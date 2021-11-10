

int numberOfHarmonics = 150;

public class Collision{
    public int[] Multiples {get; set;}
    public float Frequency {get; set;}

    public Collision(int[] multiples, float frequency){
        Multiples = multiples;
        Frequency = frequency;
    }
}

public void Main(){
    int numFreqs;
    float[] freqs;
    numFreqs, freqs = Frequencies();
}

public float[] Frequencies(){
    int numFreqs = -1
    console.writeline("How many frequencies would you like to compare?");
    do
    {
        try{
            numFreqs = int(console.readline());
        }
        catch{
            console.writeline("Please enter an integer greater than 1:");
        }
    } while (numFreqs < 2);

    float[] freqs = new float[numFreqs];
    for (int i = 0; i < numFreqs; i++){
        console.writeline($"Enter frequency {i}: ");
        freqs[i] = console.readline();
    }

    return numFreqs, freqs
}

public Collision[] CollisionDetection(int numFrequencies, float[] frequencies){
    Collision[] collisions = new Collision[numFrequencies, ];
    float[] allFreqs = new float[numFrequencies, numberOfHarmonics];

    for (int i = 0; i < numFreqs; i++){
        for (int j = 0; j < numberOfHarmonics; j++)[
            allFreqs[i,j] = frequencies[i] * (j+1);
        ]
    }


    return collisions;
}

Main()