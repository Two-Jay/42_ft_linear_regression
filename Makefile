CC = python3

TRAINER_PATH = "./trainer"
PREDICTOR_PATH = "./predictor"

train:
	@$(CC) $(TRAINER_PATH)/trainer.py

predict:
	@$(CC) $(PREDICTOR_PATH)/predictor.py

clean:
	rm -rf $(TRAINER_PATH)/__pycache__
	rm -rf $(PREDICTOR_PATH)/__pycache__

.PHONY: train predict clean