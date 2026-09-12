#!/usr/bin/env python3
"""
🚀 INSTALLATION INTERACTIVE - RENDER POUR TÉLÉPHONE
Guide pas-à-pas avec vérification automatique
"""

import os
import sys
import subprocess
import time
from datetime import datetime

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_banner():
    print(f"""
{Colors.CYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║       📱 AVIATOR PREDICTOR CONGO BET - INSTALLATION TÉLÉPHONE║
║                                                               ║
║              🚀 DÉPLOIEMENT RENDER (15 MINUTES)              ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
{Colors.END}
""")

def print_step(step_num, title):
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}{'='*65}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.GREEN}ÉTAPE {step_num}: {title}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}{'='*65}{Colors.END}\n")

def print_info(text):
    print(f"{Colors.CYAN}ℹ️  {text}{Colors.END}")

def print_success(text):
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

def print_error(text):
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_code(code):
    print(f"{Colors.BOLD}{Colors.WHITE}  {code}{Colors.END}")

def pause():
    input(f"\n{Colors.BOLD}{Colors.YELLOW}Appuyez ENTER pour continuer...{Colors.END}")

def check_github():
    """Vérifier si le repo GitHub existe"""
    print_step(1, "VÉRIFICATION - Repo GitHub")
    
    print_info("Vérification du repository GitHub...")
    print_code("ngotenirudydan81-dot/aviator-predictor-congo-bet")
    
    try:
        result = subprocess.run(
            ["git", "ls-remote", "--heads", 
             "https://github.com/ngotenirudydan81-dot/aviator-predictor-congo-bet.git"],
            capture_output=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print_success("Repository trouvé et accessible!")
            return True
        else:
            print_error("Repository non trouvé")
            return False
    except Exception as e:
        print_warning(f"Impossible de vérifier: {str(e)}")
        print_info("Continuons quand même...")
        return True

def step_github_account():
    """Étape 1: Créer compte GitHub"""
    print_step(1, "CRÉER COMPTE GITHUB (si nécessaire)")
    
    print(f"{Colors.BOLD}Si vous n'avez pas de compte GitHub:{Colors.END}")
    print("\n  1. Allez sur https://github.com")
    print("  2. Cliquez 'Sign up'")
    print("  3. Remplissez les champs")
    print("  4. Vérifiez votre email")
    print("  5. Vous êtes prêt!")
    
    print(f"\n{Colors.BOLD}✓ Vous avez un compte GitHub?{Colors.END}")
    pause()

def step_create_render():
    """Étape 2: Créer compte Render"""
    print_step(2, "CRÉER COMPTE RENDER (GRATUIT)")
    
    print(f"{Colors.BOLD}Render c'est:{Colors.END}")
    print(f"  {Colors.GREEN}✅ Gratuit: 750 heures/mois{Colors.END}")
    print(f"  {Colors.GREEN}✅ Toujours en ligne 24/7{Colors.END}")
    print(f"  {Colors.GREEN}✅ SSL automatique{Colors.END}")
    print(f"  {Colors.GREEN}✅ Pas de carte bancaire requise{Colors.END}")
    print(f"  {Colors.GREEN}✅ Accessible depuis n'importe où{Colors.END}")
    
    print(f"\n{Colors.BOLD}Étapes:{Colors.END}")
    print("\n  1. Allez sur https://render.com")
    print("  2. Cliquez 'Get Started'")
    print("  3. Choisissez 'Sign up with GitHub'")
    print("  4. Autorisez Render à accéder GitHub")
    print("  5. Complétez votre profil")
    
    print(f"\n{Colors.BOLD}Vous avez créé un compte Render?{Colors.END}")
    pause()

def step_connect_github():
    """Étape 3: Connecter GitHub à Render"""
    print_step(3, "CONNECTER GITHUB À RENDER")
    
    print(f"{Colors.BOLD}Donnez accès à votre repository:{Colors.END}")
    
    print("\n  1. Render Dashboard → Settings (en bas)")
    print("  2. Connecter un nouveau service")
    print("  3. Sélectionnez GitHub")
    print("  4. Autorisez Render")
    print("  5. Sélectionnez 'aviator-predictor-congo-bet'")
    
    print(f"\n{Colors.CYAN}💡 Render peut accéder votre repo?{Colors.END}")
    pause()

def step_create_web_service():
    """Étape 4: Créer Web Service"""
    print_step(4, "CRÉER WEB SERVICE")
    
    print(f"{Colors.BOLD}Nouveau Web Service:{Colors.END}")
    
    print("\n  1. Render Dashboard → '+ New +'")
    print("  2. Sélectionnez 'Web Service'")
    print("  3. Choisissez 'Build from existing Git repo'")
    print("  4. Sélectionnez 'aviator-predictor-congo-bet'")
    print("  5. Cliquez 'Connect'")
    
    print(f"\n{Colors.BOLD}Vous voyez votre repository?{Colors.END}")
    pause()

def step_configure_service():
    """Étape 5: Configurer le service"""
    print_step(5, "CONFIGURER LE SERVICE")
    
    print(f"{Colors.BOLD}Remplissez les champs:{Colors.END}")
    
    print(f"\n{Colors.YELLOW}Name:{Colors.END}")
    print("  aviator-predictor-congo-bet")
    
    print(f"\n{Colors.YELLOW}Environment:{Colors.END}")
    print("  Python 3")
    
    print(f"\n{Colors.YELLOW}Region:{Colors.END}")
    print("  Choisissez la région la plus proche de vous")
    
    print(f"\n{Colors.YELLOW}Branch:{Colors.END}")
    print("  main")
    
    print(f"\n{Colors.YELLOW}Build Command:{Colors.END}")
    print_code("pip install -r requirements.txt")
    
    print(f"\n{Colors.YELLOW}Start Command:{Colors.END}")
    print_code("gunicorn --bind 0.0.0.0:$PORT wsgi:app")
    
    print(f"\n{Colors.BOLD}Configuration complète?{Colors.END}")
    pause()

def step_instance_type():
    """Étape 6: Choisir Instance Type"""
    print_step(6, "CHOISIR INSTANCE TYPE")
    
    print(f"{Colors.BOLD}IMPORTANT - Sélectionnez FREE:{Colors.END}")
    
    print(f"\n{Colors.GREEN}✅ FREE (Gratuit){Colors.END}")
    print("  • Gratuit: 750 heures/mois")
    print("  • Parfait pour commencer")
    print("  • Peut être upgrader plus tard")
    
    print(f"\n{Colors.RED}❌ NE PAS CHOISIR:{Colors.END}")
    print("  • Standard/Pro (payant)")
    
    print(f"\n{Colors.BOLD}Vous avez choisi FREE?{Colors.END}")
    pause()

def step_environment_variables():
    """Étape 7: Variables d'environnement"""
    print_step(7, "VARIABLES D'ENVIRONNEMENT")
    
    print(f"{Colors.BOLD}Ajouter variables (optionnel mais recommandé):{Colors.END}")
    
    print(f"\n{Colors.YELLOW}Variable 1:{Colors.END}")
    print("  KEY: FLASK_ENV")
    print("  VALUE: production")
    
    print(f"\n{Colors.CYAN}💡 Cliquez 'Add Environment Variable'{Colors.END}")
    
    print(f"\n{Colors.BOLD}Variables ajoutées?{Colors.END}")
    pause()

def step_deploy():
    """Étape 8: Déployer"""
    print_step(8, "DÉPLOIEMENT")
    
    print(f"{Colors.BOLD}C'est prêt! Cliquez pour déployer:{Colors.END}")
    
    print("\n  Cliquez le bouton: 'Create Web Service'")
    
    print(f"\n{Colors.YELLOW}Render va:{Colors.END}")
    print("  📥 1. Cloner votre repository")
    print("  📦 2. Installer les dépendances (2-3 min)")
    print("  🔨 3. Compiler l'application")
    print("  🚀 4. Lancer le serveur")
    
    print(f"\n{Colors.BOLD}Attendez le déploiement...{Colors.END}")
    print(f"{Colors.CYAN}Vous verrez l'état en temps réel dans le dashboard{Colors.END}")
    
    pause()

def step_wait_deployment():
    """Étape 9: Attendre déploiement"""
    print_step(9, "ATTENDRE LE DÉPLOIEMENT")
    
    print(f"{Colors.BOLD}États du déploiement:{Colors.END}")
    
    print(f"\n{Colors.YELLOW}🔵 Building...{Colors.END} (2-3 minutes)")
    print("  Render installe les dépendances")
    
    print(f"\n{Colors.YELLOW}🟡 Deploying...{Colors.END} (30 secondes)")
    print("  Render lance l'application")
    
    print(f"\n{Colors.GREEN}🟢 Live{Colors.END}")
    print("  ✅ Votre app est en ligne!")
    
    print(f"\n{Colors.CYAN}💡 Si ça prend plus de 10 min, il y a peut-être un problème{Colors.END}")
    print(f"{Colors.CYAN}   Consultez les logs: Dashboard → Logs{Colors.END}")
    
    print(f"\n{Colors.BOLD}Vous voyez 'Live'?{Colors.END}")
    pause()

def step_get_url():
    """Étape 10: Obtenir l'URL"""
    print_step(10, "OBTENIR VOTRE URL")
    
    print(f"{Colors.BOLD}Votre URL est affichée en haut:{Colors.END}")
    
    print(f"\n{Colors.YELLOW}Ressemble à:{Colors.END}")
    print_code("https://aviator-predictor-congo-bet.onrender.com")
    
    print(f"\n{Colors.CYAN}💡 Copier cette URL - vous en aurez besoin!{Colors.END}")
    
    print(f"\n{Colors.BOLD}Vous avez l'URL?{Colors.END}")
    input(f"{Colors.YELLOW}Collez-la ici: {Colors.END}")

def step_access_mobile():
    """Étape 11: Accéder sur téléphone"""
    print_step(11, "ACCÉDER SUR TÉLÉPHONE")
    
    print(f"{Colors.BOLD}Sur votre téléphone:{Colors.END}")
    
    print(f"\n{Colors.YELLOW}iPhone - Safari:{Colors.END}")
    print("  1. Ouvrez Safari")
    print("  2. Collez votre URL Render")
    print("  3. Appuyez 'Go'")
    print("  4. 🎉 Vous y êtes!")
    
    print(f"\n{Colors.YELLOW}Android - Chrome:{Colors.END}")
    print("  1. Ouvrez Chrome")
    print("  2. Collez votre URL Render")
    print("  3. Appuyez 'Go'")
    print("  4. 🎉 Vous y êtes!")
    
    print(f"\n{Colors.BOLD}Ajouter à l'écran d'accueil:{Colors.END}")
    
    print(f"\n{Colors.YELLOW}iPhone:{Colors.END}")
    print("  1. Partager → Ajouter à l'écran d'accueil")
    print("  2. Nommez: 'Aviator Predictor'")
    print("  3. Ajouter")
    
    print(f"\n{Colors.YELLOW}Android:{Colors.END}")
    print("  1. Menu ⋮ → Ajouter à l'écran d'accueil")
    print("  2. Nommez: 'Aviator Predictor'")
    print("  3. Ajouter")
    
    print(f"\n{Colors.BOLD}L'app charge sur votre téléphone?{Colors.END}")
    pause()

def step_verify():
    """Étape 12: Vérifier que ça marche"""
    print_step(12, "VÉRIFIER LES FONCTIONNALITÉS")
    
    print(f"{Colors.BOLD}Sur votre téléphone, vérifiez:{Colors.END}")
    
    print(f"\n{Colors.YELLOW}1. Dashboard charge:{Colors.END}")
    print(f"   {Colors.GREEN}✅ Logo 'Aviator Predictor'{Colors.END}")
    
    print(f"\n{Colors.YELLOW}2. Statistiques visibles:{Colors.END}")
    print(f"   {Colors.GREEN}✅ Total Games, Crash Rate, etc.{Colors.END}")
    
    print(f"\n{Colors.YELLOW}3. Prédictions affichées:{Colors.END}")
    print(f"   {Colors.GREEN}✅ Next Multiplier, Crash Probability{Colors.END}")
    
    print(f"\n{Colors.YELLOW}4. Graphiques visibles:{Colors.END}")
    print(f"   {Colors.GREEN}✅ Charts avec les jeux récents{Colors.END}")
    
    print(f"\n{Colors.YELLOW}5. Feed des jeux:{Colors.END}")
    print(f"   {Colors.GREEN}✅ Jeux en temps réel avec status{Colors.END}")
    
    print(f"\n{Colors.BOLD}Tout fonctionne?{Colors.END}")
    pause()

def final_summary():
    """Résumé final"""
    print_step("✅", "INSTALLATION RÉUSSIE!")
    
    print(f"""
{Colors.BOLD}{Colors.GREEN}
╔═══════════════════════════════════════════════════════════════╗
║                  🎉 FÉLICITATIONS! 🎉                        ║
║                                                               ║
║   Votre Aviator Predictor est maintenant accessible sur      ║
║   votre téléphone 24/7!                                      ║
╚═══════════════════════════════════════════════════════════════╝
{Colors.END}
    """)
    
    print(f"{Colors.BOLD}Prochaines étapes:{Colors.END}")
    
    print(f"\n{Colors.CYAN}1. 📊 Analyser les prédictions{Colors.END}")
    print("   Observez les patterns sur plusieurs jours")
    
    print(f"\n{Colors.CYAN}2. 🧠 Améliorer le ML{Colors.END}")
    print("   Plus de données = meilleures prédictions")
    
    print(f"\n{Colors.CYAN}3. 📱 Partager{Colors.END}")
    print("   Invitez vos amis à utiliser l'app")
    
    print(f"\n{Colors.CYAN}4. 🔧 Personnaliser{Colors.END}")
    print("   Fork le repo, modifiez, redéployez")
    
    print(f"\n{Colors.BOLD}Besoin d'aide?{Colors.END}")
    print("  📖 Consultez MOBILE_GUIDE.md")
    print("  🐛 Signallez les bugs sur GitHub Issues")
    print("  💬 Posez des questions dans Discussions")
    
    print(f"\n{Colors.BOLD}Merci d'utiliser Aviator Predictor!{Colors.END}")
    print(f"{Colors.BOLD}Bon prédiction! 🎮{Colors.END}\n")

def main():
    """Programme principal"""
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print_banner()
    
    # Vérifications
    print_info("Vérification des prérequis...")
    if not check_github():
        print_warning("Continuons quand même...")
    
    pause()
    
    # Étapes
    step_github_account()
    step_create_render()
    step_connect_github()
    step_create_web_service()
    step_configure_service()
    step_instance_type()
    step_environment_variables()
    step_deploy()
    step_wait_deployment()
    step_get_url()
    step_access_mobile()
    step_verify()
    
    # Résumé
    final_summary()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Installation annulée.{Colors.END}")
        sys.exit(0)
