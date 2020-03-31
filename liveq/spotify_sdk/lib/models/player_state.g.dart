// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'player_state.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

PlayerState _$PlayerStateFromJson(Map<String, dynamic> json) {
  return PlayerState(
    json['track'] == null
        ? null
        : Track.fromJson(json['track'] as Map<String, dynamic>),
    json['is_paused'] as bool,
    (json['playback_speed'] as num)?.toDouble(),
    json['playback_position'] as int,
    json['playback_options'] == null
        ? null
        : PlayerOptions.fromJson(
            json['playback_options'] as Map<String, dynamic>),
    json['playback_restrictions'] == null
        ? null
        : PlayerRestrictions.fromJson(
            json['playback_restrictions'] as Map<String, dynamic>),
  );
}

Map<String, dynamic> _$PlayerStateToJson(PlayerState instance) =>
    <String, dynamic>{
      'track': instance.track,
      'is_paused': instance.isPaused,
      'playback_speed': instance.playbackSpeed,
      'playback_position': instance.playbackPosition,
      'playback_options': instance.playbackOptions,
      'playback_restrictions': instance.playbackRestrictions,
    };
