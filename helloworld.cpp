#include <fstream>
#include <iostream>
#include <speechapi_cxx.h>

using namespace std;
using namespace Microsoft::CognitiveServices::Speech;

void synthesizeSpeech()
{
	// Creates an instance of a speech config with specified subscription key and service region.
	// Replace with your own subscription key and service region (e.g., "westus").
	auto config = SpeechConfig::FromSubscription("4621e53defff4a949497e3468f63c4c8", "eastus");

	// Creates a speech synthesizer using the default speaker as audio output. The default spoken language is "en-us".
	auto synthesizer = SpeechSynthesizer::FromConfig(config);

	// Receive a text from console input and synthesize it to speaker
	std::string text;
	ifstream file; // declares file to read from
	file.open("lines_to_synth"); // opens the file
	std::getline(file, text); // gets the first line in the file

	auto result = synthesizer->SpeakTextAsync(text).get();

	// Checks result.
	if (result->Reason == ResultReason::SynthesizingAudioCompleted)
	{
		cout << "Speech synthesized to speaker for text [" << text << "]" << std::endl;
	}
	else if (result->Reason == ResultReason::Canceled)
	{
		auto cancellation = SpeechSynthesisCancellationDetails::FromResult(result);
		cout << "CANCELED: Reason=" << (int)cancellation->Reason << std::endl;

		if (cancellation->Reason == CancellationReason::Error)
		{
			cout << "CANCELED: ErrorCode=" << (int)cancellation->ErrorCode << std::endl;
			cout << "CANCELED: ErrorDetails=[" << cancellation->ErrorDetails << "]" << std::endl;
			cout << "CANCELED: Did you update the subscription info?" << std::endl;
		}
	}

	// This is to give some time for the speaker to finish playing back the audio
	//cout << "Press enter to exit..." << std::endl;
	//cin.get();
	for (int i=0; i<1000; i++) {

	}
}

int main()
{
	synthesizeSpeech();
	return 0;
}


