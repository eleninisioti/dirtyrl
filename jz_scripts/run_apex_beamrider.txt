#!/bin/bash
#SBATCH -J beamrdiderapex
#SBATCH --nodes=16
#SBATCH -t 200:00:00
#SBATCH --ntasks-per-node=10
#SBATCH --output=/scratch/enisioti/cleanrl_log/jz_logs/%j.out
#SBATCH --error=/scratch/enisioti/cleanrl_log/jz_logs/%j.err

python cleanrl/apex_atari.py
