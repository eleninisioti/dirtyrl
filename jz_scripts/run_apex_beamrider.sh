#!/bin/bash
#SBATCH -J cleanrlapex
#SBATCH -t 48:00:00
#SBATCH --cpus-per-task 32
#SBATCH --output=/scratch/enisioti/cleanrl_log/jz_logs/%j.out
#SBATCH --error=/scratch/enisioti/cleanrl_log/jz_logs/%j.err

python cleanrl/apex_atari.py
