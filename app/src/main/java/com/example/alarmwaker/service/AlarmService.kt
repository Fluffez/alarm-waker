package com.example.alarmwaker.service

import android.app.Service
import android.content.Intent
import android.media.AudioAttributes
import android.media.RingtoneManager
import android.os.Build
import android.os.Handler
import android.os.IBinder
import android.os.Looper
import android.util.Log
import androidx.core.app.NotificationCompat
import com.example.alarmwaker.MainActivity
import com.example.alarmwaker.R

class AlarmService : Service() {

    private var isAlarmPlaying = false
    private val handler = Handler(Looper.getMainLooper())
    private var ringtone: android.media.Ringtone? = null

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        Log.d(TAG, "AlarmService started")
        
        val alarmType = intent?.getStringExtra("alarm_type") ?: "default"
        val duration = intent?.getLongExtra("duration", 30000L) ?: 30000L
        
        playAlarm(alarmType, duration)
        
        return START_STICKY
    }

    private fun playAlarm(alarmType: String, duration: Long) {
        if (isAlarmPlaying) {
            Log.d(TAG, "Alarm already playing")
            return
        }

        isAlarmPlaying = true
        
        // Show notification
        val notification = NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle("Alarm!")
            .setContentText("Arkadaşınız seni uyandırmaya çalışıyor!")
            .setSmallIcon(R.drawable.ic_launcher_foreground)
            .setAutoCancel(true)
            .setContentIntent(
                android.app.PendingIntent.getActivity(
                    this,
                    0,
                    Intent(this, MainActivity::class.java),
                    android.app.PendingIntent.FLAG_UPDATE_CURRENT or android.app.PendingIntent.FLAG_IMMUTABLE
                )
            )
            .build()

        startForeground(NOTIFICATION_ID, notification)

        // Play ringtone
        try {
            val ringtoneUri = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_ALARM)
            ringtone = RingtoneManager.getRingtone(this, ringtoneUri)
            
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
                ringtone?.setLooping(true)
                val audioAttributes = AudioAttributes.Builder()
                    .setUsage(AudioAttributes.USAGE_ALARM)
                    .build()
                ringtone?.audioAttributes = audioAttributes
            }
            
            ringtone?.play()
            Log.d(TAG, "Alarm playing")
        } catch (e: Exception) {
            Log.e(TAG, "Error playing alarm", e)
        }

        // Stop alarm after duration
        handler.postDelayed({
            stopAlarm()
        }, duration)
    }

    private fun stopAlarm() {
        Log.d(TAG, "Stopping alarm")
        isAlarmPlaying = false
        
        try {
            ringtone?.stop()
        } catch (e: Exception) {
            Log.e(TAG, "Error stopping alarm", e)
        }
        
        stopForeground(STOP_FOREGROUND_REMOVE)
        stopSelf()
    }

    override fun onBind(intent: Intent?): IBinder? = null

    companion object {
        private const val TAG = "AlarmService"
        private const val NOTIFICATION_ID = 1
        private const val CHANNEL_ID = "alarm_channel"
    }
}
