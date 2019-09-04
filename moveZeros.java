import java.util.Arrays;

class moveZeros {
    public static void main(String[] args) {
        int[] nums = new int[]{0, 1, 0, 3, 12}; //array of integers
        int [] sortedArray = new moveZeros().moveZeros(nums); //call function to sort list
        System.out.println(Arrays.toString(sortedArray));
    }//end of main()

    public int[] moveZeros(int[] array){
        //moving
        int[] sorted = new int[array.length];
        int forwardIndex = 0;//start writing non-zero element from 0
        int backwardIndex = array.length-1;//this index iterates from the last element
        for (int i = 0; i < array.length; i++){//iterate until the mid of the array
            System.out.println("ROUND " + i + ": " + array[i]);
            if (array[i] == 0) {//if the element is 0
                //sorted[backwardIndex] = array[i];
                backwardIndex--; //move the interator to a digit before it after assigned element to 0
                }//elihw
            else {
                sorted[forwardIndex] = array[i];//write i to the left of the array
                forwardIndex++; //move to the right
            }//esle
        }//rof
        return sorted;
    }//end of moveZeros
}