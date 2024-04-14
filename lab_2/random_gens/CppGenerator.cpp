#include <iostream>
#include <random>
#include <string>

using namespace std;

/*!
  @brief the function will return a random sequence
  @param len, from, to length of the sequence and range for elements
  @return random integer sequense
 */
string random_sequence(size_t len, int from, int to)
{
	string result = "";
	for (int i = 0; i < len; i++)
	{
		random_device random_device;
		mt19937 generator(random_device());
		uniform_int_distribution<> distribution(from, to);
		result += to_string(distribution(generator));
	}
	return result;
}

int main()
{
	cout << random_sequence(128, 0, 1);
	return 0;
}