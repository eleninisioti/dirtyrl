#!/bin/bash
#SBATCH -J beamrdiderapex
#SBATCH -t 24:00:00
#SBATCH --cpus-per-task 64
#SBATCH --output=/scratch/enisioti/cleanrl_log/jz_logs/%j.out
#SBATCH --error=/scratch/enisioti/cleanrl_log/jz_logs/%j.err

python cleanrl/apex_atari.py
