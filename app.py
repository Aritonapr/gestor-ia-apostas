import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==============================================================================
# [COFRE VISUAL v58.7 - BLINDAGEM DE INTERFACE - NÃO ALTERAR ESTA SEÇÃO]
# ==============================================================================
def aplicar_layout_blindado():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
        ::-webkit-scrollbar { display: none !important; }
        * { -ms-overflow-style: none !important; scrollbar-width: none !important; }
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
            background-color: #0b0e11 !important;
            font-family: 'Inter', sans-serif;
        }
        header, [data-testid="stHeader"] { display: none !important; height: 0px !important; }
        [data-testid="stSidebarCollapseButton"] { display: none !important; }
        [data-testid="stMainBlockContainer"] { padding: 85px 40px 20px 40px !important; }
        .betano-header { 
            position: fixed; top: 0; left: 0; width: 100%; height: 60px; 
            background-color: #001a4d !important; border-bottom: 1px solid rgba(255,255,255,0.05) !important; 
            display: flex; align-items: center; justify-content: space-between; 
            padding: 0 40px !important; z-index: 1000000; 
            transform: translate3d(0,0,0); -webkit-backface-visibility: hidden;
        }
        .header-left { display: flex; align-items: center; gap: 25px; }
        .logo-link { color: #9d54ff !important; font-weight: 900; font-size: 21px !important; text-transform: uppercase; letter-spacing: 0.5px; text-decoration: none; cursor: pointer;}
        .logo-link:hover { filter: brightness(1.2); }
        .nav-links { display: flex; gap: 22px; align-items: center; }
        .nav-item { color: #ffffff !important; font-size: 11px !important; text-transform: uppercase; opacity: 1 !important; font-weight: 600 !important; letter-spacing: 0.5px; transition: 0.3s ease; cursor: pointer; white-space: nowrap; }
