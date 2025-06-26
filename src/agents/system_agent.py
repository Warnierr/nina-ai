#!/usr/bin/env python3
"""
⚙️ System Agent - Agent spécialisé en informations système
"""

import os
import psutil
import platform
from datetime import datetime
from .base_agent import BaseAgent

class SystemAgent(BaseAgent):
    """Agent spécialisé en informations système et administration"""
    
    def __init__(self):
        super().__init__("SystemAgent", "Système et administration")
        
        # Commandes système supportées
        self.system_commands = {
            "système": self._get_system_info,
            "system": self._get_system_info,
            "cpu": self._get_cpu_info,
            "processeur": self._get_cpu_info,
            "mémoire": self._get_memory_info,
            "memory": self._get_memory_info,
            "ram": self._get_memory_info,
            "disque": self._get_disk_info,
            "disk": self._get_disk_info,
            "réseau": self._get_network_info,
            "network": self._get_network_info,
            "processus": self._get_process_info,
            "process": self._get_process_info,
            "uptime": self._get_uptime,
            "température": self._get_temperature,
            "temperature": self._get_temperature,
        }
    
    def can_handle(self, query: str) -> bool:
        """Détermine si cette requête concerne le système"""
        query_clean = query.lower().strip()
        
        # Vérifier les commandes système
        if any(cmd in query_clean for cmd in self.system_commands.keys()):
            return True
        
        # Mots-clés système
        system_keywords = [
            "info", "information", "status", "état", "performance",
            "utilisation", "usage", "monitoring", "surveillance",
            "os", "linux", "ubuntu", "windows"
        ]
        
        return any(keyword in query_clean for keyword in system_keywords)
    
    def process(self, query: str) -> str:
        """Traite les requêtes système"""
        query_clean = query.lower().strip()
        
        # Exécuter la commande système appropriée
        for cmd, func in self.system_commands.items():
            if cmd in query_clean:
                try:
                    return func()
                except Exception as e:
                    return f"❌ Erreur système : {str(e)}"
        
        # Information système générale
        if any(word in query_clean for word in ["info", "information", "status", "état"]):
            return self._get_system_overview()
        
        return "⚙️ Je peux fournir des infos sur : système, CPU, mémoire, disque, réseau, processus"
    
    def _get_system_info(self) -> str:
        """Informations système générales"""
        system = platform.system()
        release = platform.release()
        version = platform.version()
        architecture = platform.machine()
        hostname = platform.node()
        
        return f"""💻 **INFORMATIONS SYSTÈME**
🖥️  OS : {system} {release}
🏗️  Architecture : {architecture}
🌐 Nom d'hôte : {hostname}
📅 Version : {version[:50]}..."""
    
    def _get_cpu_info(self) -> str:
        """Informations CPU"""
        cpu_count = psutil.cpu_count()
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_freq = psutil.cpu_freq()
        
        freq_info = f"⚡ Fréquence : {cpu_freq.current:.0f} MHz" if cpu_freq else ""
        
        return f"""🔧 **INFORMATIONS CPU**
💎 Cœurs : {cpu_count}
📊 Utilisation : {cpu_percent}%
{freq_info}"""
    
    def _get_memory_info(self) -> str:
        """Informations mémoire"""
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        return f"""🧠 **INFORMATIONS MÉMOIRE**
💾 RAM Totale : {self._bytes_to_gb(memory.total)} GB
✅ RAM Disponible : {self._bytes_to_gb(memory.available)} GB  
📊 RAM Utilisée : {memory.percent}%
🔄 SWAP : {self._bytes_to_gb(swap.total)} GB ({swap.percent}% utilisé)"""
    
    def _get_disk_info(self) -> str:
        """Informations disque"""
        disk_usage = psutil.disk_usage('/')
        
        return f"""💽 **INFORMATIONS DISQUE**
📦 Espace Total : {self._bytes_to_gb(disk_usage.total)} GB
✅ Espace Libre : {self._bytes_to_gb(disk_usage.free)} GB
📊 Utilisé : {(disk_usage.used / disk_usage.total * 100):.1f}%"""
    
    def _get_network_info(self) -> str:
        """Informations réseau"""
        try:
            net_io = psutil.net_io_counters()
            return f"""🌐 **INFORMATIONS RÉSEAU**
📡 Bytes envoyés : {self._bytes_to_mb(net_io.bytes_sent)} MB
📥 Bytes reçus : {self._bytes_to_mb(net_io.bytes_recv)} MB
📤 Paquets envoyés : {net_io.packets_sent:,}
📨 Paquets reçus : {net_io.packets_recv:,}"""
        except:
            return "🌐 Informations réseau non disponibles"
    
    def _get_process_info(self) -> str:
        """Informations processus"""
        process_count = len(psutil.pids())
        top_processes = []
        
        try:
            # Top 3 processus par CPU
            processes = [(p.info['pid'], p.info['name'], p.info['cpu_percent']) 
                        for p in psutil.process_iter(['pid', 'name', 'cpu_percent'])]
            top_processes = sorted(processes, key=lambda x: x[2] if x[2] else 0, reverse=True)[:3]
        except:
            pass
        
        result = f"""⚡ **INFORMATIONS PROCESSUS**
📊 Nombre total : {process_count}
🔥 Top processus (CPU) :"""
        
        for pid, name, cpu in top_processes:
            result += f"\n   • {name} (PID {pid}) : {cpu}%"
        
        return result
    
    def _get_uptime(self) -> str:
        """Temps de fonctionnement"""
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.now() - boot_time
        
        return f"""⏰ **TEMPS DE FONCTIONNEMENT**
🚀 Démarrage : {boot_time.strftime('%Y-%m-%d %H:%M:%S')}
⏱️  Uptime : {str(uptime).split('.')[0]}"""
    
    def _get_temperature(self) -> str:
        """Température système (si disponible)"""
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                result = "🌡️ **TEMPÉRATURES**\n"
                for name, entries in temps.items():
                    for entry in entries:
                        result += f"🔥 {entry.label or name} : {entry.current}°C\n"
                return result.strip()
            else:
                return "🌡️ Capteurs de température non disponibles"
        except:
            return "🌡️ Informations de température non accessibles"
    
    def _get_system_overview(self) -> str:
        """Vue d'ensemble du système"""
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        return f"""📊 **APERÇU SYSTÈME**
💻 OS : {platform.system()} {platform.release()}
🔧 CPU : {cpu}% utilisé
🧠 RAM : {memory.percent}% utilisée ({self._bytes_to_gb(memory.available)} GB libre)
💽 Disque : {(disk.used / disk.total * 100):.1f}% utilisé"""
    
    def _bytes_to_gb(self, bytes_value: int) -> float:
        """Convertit bytes en GB"""
        return round(bytes_value / (1024**3), 2)
    
    def _bytes_to_mb(self, bytes_value: int) -> float:
        """Convertit bytes en MB"""
        return round(bytes_value / (1024**2), 2) 