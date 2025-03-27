import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

mu = st.slider("μ (Mean)", -10.0, 10.0, 0.0)
sigma = st.slider("σ (Standard Deviation)", 0.1, 10.0, 1.0)

def p(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

x = np.linspace(-15, 15, 1000)
y = p(x, mu, sigma)

fig, ax = plt.subplots()
ax.axhline(0, color="yellow", linewidth=2)  
ax.axvline(0, color="yellow", linewidth=2)  
ax.plot(x, y, color="blue", label=f"μ = {mu}, σ = {sigma}")
ax.set_xlabel("x")
ax.set_ylabel("Probability Density")
ax.set_title("Gaussian Mass Function")
ax.legend()
ax.grid()

st.pyplot(fig)
