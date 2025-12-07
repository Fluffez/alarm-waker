package com.example.alarmwaker.receiver

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.util.Log
import com.example.alarmwaker.service.AlarmService

class AlarmReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context?, intent: Intent?) {
        Log.d(TAG, "AlarmReceiver triggered")
        
        context?.let {
            val alarmType = intent?.getStringExtra("alarm_type") ?: "default"
            val duration = intent?.getLongExtra("duration", 30000L) ?: 30000L
            
            val serviceIntent = Intent(it, AlarmService::class.java).apply {
                putExtra("alarm_type", alarmType)
                putExtra("duration", duration)
            }
            
            it.startService(serviceIntent)
        }
    }

    companion object {
        private const val TAG = "AlarmReceiver"
    }
}
