"""
Script d'exécution pour la bibliothèque surf_scrap avec arguments en ligne de commande
"""

import surf_scrap
import argparse
import sys
import os

def main():
    """
    Fonction principale avec support des arguments en ligne de commande
    """
    
    # Configuration du parser d'arguments
    parser = argparse.ArgumentParser(
        description=' Extraction des données météo surf depuis surf-report.com',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation :
  # Mode interactif
  python run_surf_scrap.py
  
  # Avec arguments
  python run_surf_scrap.py -u https://www.surf-report.com/meteo-surf/lacanau-s1043.html -o data/lacanau.csv
  
  # Version courte
  python run_surf_scrap.py -u URL -o output.csv

URLs supportées :
  - Lacanau: https://www.surf-report.com/meteo-surf/lacanau-s1043.html
  - Carcans: https://www.surf-report.com/meteo-surf/carcans-plage-s1013.html
  - Moliets: https://www.surf-report.com/meteo-surf/moliets-plage-centrale-s102799.html
        """
    )
    
    parser.add_argument(
        '-u', '--url',
        type=str,
        help='URL de la page surf-report.com',
        required=False
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='surf_data.csv',
        help='Chemin du fichier CSV de sortie (défaut: surf_data.csv)',
        required=False
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Mode verbeux (afficher plus de détails)'
    )
    
    # Parser les arguments
    args = parser.parse_args()
    
    # Si aucun argument n'est fourni, passer en mode interactif
    if not args.url:
        mode_interactif()
    else:
        mode_automatique(args.url, args.output, args.verbose)


def mode_interactif():
    """
    Mode interactif : demande les informations à l'utilisateur
    """
    print("=" * 80)
    print("   SURF SCRAP - Extraction des données météo surf")
    print("=" * 80)
    print()
    
    # Demander l'URL
    print(" Entrez l'URL de la page surf-report.com")
    print("   Exemples :")
    print("   - https://www.surf-report.com/meteo-surf/lacanau-s1043.html")
    print("   - https://www.surf-report.com/meteo-surf/carcans-plage-s1013.html")
    print()
    
    url = input("URL : ").strip()
    
    if not url:
        print(" Erreur : L'URL ne peut pas être vide.")
        sys.exit(1)
    
    # Demander le chemin de sortie
    print()
    print(" Entrez le chemin où sauvegarder le fichier CSV")
    print("   (Appuyez sur Entrée pour utiliser 'surf_data.csv' par défaut)")
    
    output_path = input("Chemin : ").strip()
    
    if not output_path:
        output_path = 'surf_data.csv'
        print(f"   → Utilisation du chemin par défaut : {output_path}")
    
    print()
    print("=" * 80)
    
    # Exécuter l'extraction
    executer_extraction(url, output_path, verbose=True)
    
    # Demander si continuer
    print()
    continuer = input("Voulez-vous extraire d'autres données ? (o/n) : ").strip().lower()
    
    if continuer in ['o', 'oui', 'y', 'yes']:
        print()
        mode_interactif()
    else:
        print("\n👋 Au revoir !\n")


def mode_automatique(url, output_path, verbose=False):
    """
    Mode automatique : utilise les arguments fournis
    """
    if verbose:
        print("=" * 80)
        print("   SURF SCRAP - Mode automatique")
        print("=" * 80)
        print(f"\n URL : {url}")
        print(f" Sortie : {output_path}\n")
        print("=" * 80)
    
    executer_extraction(url, output_path, verbose)


def executer_extraction(url, output_path, verbose=True):
    """
    Exécute l'extraction des données
    """
    try:
        # CORRECTION : Création automatique du dossier parent si nécessaire
        parent_dir = os.path.dirname(output_path)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
            if verbose:
                print(f"📁 Dossier '{parent_dir}' créé avec succès.")

        # Appel de la fonction de la bibliothèque installée
        df = surf_scrap.extract_surf_data(url, output_path)
        
        if verbose:
            print()
            print("=" * 80)
            print("   EXTRACTION RÉUSSIE !")
            print("=" * 80)
            print("\n Aperçu des données (5 premières lignes) :")
            print()
            print(df.head(5).to_string())
            print()
            print(f" Total : {len(df)} prévisions extraites")
            print(f" Fichier sauvegardé : {os.path.abspath(output_path)}")
            print()
        else:
            print(f"✅ Extraction réussie : {len(df)} prévisions → {output_path}")
        
        return df

    except ValueError as e:
        print(f"\n❌ ERREUR DE VALIDATION :\n   {e}")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ ERREUR LORS DE L'EXTRACTION :\n   {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()